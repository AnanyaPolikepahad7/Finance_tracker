import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
from datetime import datetime
import os
from runner.analyzer_runner import run_analysis_for_user
import csv


DATA_PATH = "data/transactions.csv"

# Handle form submission
def submit_form(entries, type_var, category_var, recurring_var, chart_frame):
    data = [e.get() for e in entries]
    data.append(type_var.get())
    data.append(category_var.get())
    data.append(recurring_var.get())

    user_id = data[0]
    file_path = "data/transactions.csv"
    file_exists = os.path.isfile(file_path)

    headers = ['User_ID', 'Date', 'Time', 'Amount', 'Type', 'Description', 'Merchant',
               'Category', 'Payment mode', 'Account', 'Location', 'Recurring']

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(data)

    print("✅ Transaction submitted for User:", user_id)

    # Clear previous plots
    for widget in chart_frame.winfo_children():
        widget.destroy()

    run_analysis_for_user(user_id, chart_frame)

# Launch the full UI
def upload_csv(chart_frame):
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        uploaded_df = pd.read_csv(file_path)

        required_cols = ['User_ID', 'Date', 'Time', 'Amount', 'Type', 'Description',
                         'Merchant', 'Category', 'Payment mode', 'Account', 'Location', 'Recurring']

        if not all(col in uploaded_df.columns for col in required_cols):
            messagebox.showerror("Format Error", "CSV must contain required columns.")
            return

        if os.path.exists(DATA_PATH):
            existing_df = pd.read_csv(DATA_PATH)
            combined_df = pd.concat([existing_df, uploaded_df], ignore_index=True)
        else:
            combined_df = uploaded_df

        combined_df.to_csv(DATA_PATH, index=False)
        messagebox.showinfo("Upload Successful", "CSV data saved successfully!")

        user_id = uploaded_df['User_ID'].iloc[0]

        # Clear previous plots
        for widget in chart_frame.winfo_children():
            widget.destroy()

        run_analysis_for_user(user_id, chart_frame)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process file.\n{e}")


def launch_ui():
    root = tk.Tk()
    root.title("💸 Personal Finance Tracker")
    root.geometry("600x1000")

    labels = ['User_ID', 'Date (YYYY-MM-DD)', 'Time (HH:MM)', 'Amount',
              'Description', 'Merchant', 'Payment mode', 'Account', 'Location']
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

    # 📊 Chart Frame
    chart_frame = tk.Frame(root)
    chart_frame.pack(pady=20)

    # Submit Button
    tk.Button(root, text="Submit Transaction", bg="purple", fg="white",
              command=lambda: submit_form(entries, type_var, category_var, recurring_var, chart_frame)).pack(pady=10)
    tk.Button(root, text="Upload CSV", command=lambda: upload_csv(chart_frame), bg="gray", fg="white").pack(pady=10)

    root.mainloop()
# Handle CSV Upload

# Launch the UI
