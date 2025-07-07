import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import pandas as pd
import os
import csv
from runner.analyzer_runner import run_analysis_for_user

DATA_PATH = "data/transactions.csv"

# 📂 Upload CSV and analyze by asking user ID
def upload_csv_and_analyze():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return

    try:
        df = pd.read_csv(file_path)

        required_cols = ['User_ID', 'Date', 'Time', 'Amount', 'Type', 'Description', 'Merchant',
                         'Category', 'Payment Mode', 'Account', 'Location', 'Recurring']

        if not all(col in df.columns for col in required_cols):
            messagebox.showerror("❌ Error", "CSV is missing required columns.")
            return

        existing = pd.read_csv(DATA_PATH) if os.path.exists(DATA_PATH) else pd.DataFrame(columns=required_cols)
        combined = pd.concat([existing, df], ignore_index=True)
        combined.to_csv(DATA_PATH, index=False)

        user_id = simpledialog.askstring("User ID", "Enter User ID to analyze from uploaded CSV:")
        if user_id:
            run_analysis_for_user(user_id)
        else:
            messagebox.showinfo("Cancelled", "User ID was not provided.")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# 📝 Submit transaction from form
def submit_form(entries, type_var, category_var, recurring_var):
    data = [e.get() for e in entries]
    data.append(type_var.get())
    data.append(category_var.get())
    data.append(recurring_var.get())

    # ⚠️ Check for empty fields
    if any(field.strip() == '' for field in data):
        messagebox.showwarning("⚠️ Incomplete", "Please fill in all fields before submitting.")
        return

    user_id = str(data[0]).strip().replace('.0', '')
    data[0] = user_id

    headers = ['User_ID', 'Date', 'Time', 'Amount', 'Type', 'Description', 'Merchant',
               'Category', 'Payment Mode', 'Account', 'Location', 'Recurring']

    file_exists = os.path.exists(DATA_PATH)
    with open(DATA_PATH, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(data)

    print(f"✅ Transaction submitted for User: {user_id}")
    run_analysis_for_user(user_id)

# 🚀 Launch UI
def launch_ui_form():
    root = tk.Tk()
    root.title("💸 Finance Tracker - Add Transaction")
    root.geometry("500x700")

    labels = ['User_ID', 'Date (YYYY-MM-DD)', 'Time (HH:MM)', 'Amount',
              'Description', 'Merchant', 'Payment Mode', 'Account', 'Location']
    entries = []

    for label in labels:
        tk.Label(root, text=label).pack()
        entry = tk.Entry(root, width=40)
        entry.pack(pady=5)
        entries.append(entry)

    type_var = tk.StringVar(value="Debit")
    tk.Label(root, text="Type").pack()
    tk.Radiobutton(root, text="Debit", variable=type_var, value="Debit").pack()
    tk.Radiobutton(root, text="Credit", variable=type_var, value="Credit").pack()

    category_var = tk.StringVar(value="Food & Drinks")
    tk.Label(root, text="Category").pack()
    categories = ["Food & Drinks", "Groceries", "Entertainment", "Transport", "Utilities", "Travel", "Health", "Others"]
    tk.OptionMenu(root, category_var, *categories).pack()

    recurring_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Recurring?", variable=recurring_var).pack(pady=10)

    tk.Button(root, text="Submit Transaction", bg="purple", fg="white",
              command=lambda: submit_form(entries, type_var, category_var, recurring_var)).pack(pady=10)

    tk.Button(root, text="📂 Upload CSV & Analyze", command=upload_csv_and_analyze,
              bg="orange", fg="white").pack(pady=10)

    tk.Label(root, text="Required columns:\nUser_ID, Date, Time, Amount, Type, Description,\n"
                        "Merchant, Category, Payment Mode, Account, Location, Recurring",
             fg="red", wraplength=400, justify="left").pack(pady=10)

    root.mainloop()
