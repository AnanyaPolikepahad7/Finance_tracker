# import matplotlib.pyplot as plt

# def plot_pie_chart_by_category(df, return_fig=False):
#     cat_summary = df.groupby('Category')['Amount'].sum()
#     fig, ax = plt.subplots(figsize=(6, 6))
#     ax.pie(cat_summary, labels=cat_summary.index, autopct='%1.1f%%', startangle=140)
#     ax.set_title("Expenses by Category")
#     return fig if return_fig else plt.show()

# def plot_pie_chart_by_account(df, return_fig=False):
#     acc_summary = df.groupby('Account')['Amount'].sum()
#     fig, ax = plt.subplots(figsize=(6, 6))
#     ax.pie(acc_summary, labels=acc_summary.index, autopct='%1.1f%%', startangle=140)
#     ax.set_title("Spending by Account")
#     return fig if return_fig else plt.show()

# def plot_anomalies(df, return_fig=False):
#     import seaborn as sns
#     fig, ax = plt.subplots(figsize=(8, 5))
#     sns.scatterplot(data=df, x='Date', y='Amount', hue='Is_Anomaly', ax=ax)
#     ax.set_title("Anomaly Detection")
#     ax.tick_params(axis='x', rotation=45)
#     return fig if return_fig else plt.show()
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def show_visualizations(df, user_id=None):
    window = tk.Toplevel()
    window.title(f"📊 Analysis for User {user_id}")
    window.geometry("800x800")

    # Pie chart for Category breakdown
    fig1, ax1 = plt.subplots(figsize=(5, 5))
    df['Category'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, ax=ax1)
    ax1.set_ylabel('')
    ax1.set_title("Expense Distribution by Category")
    canvas1 = FigureCanvasTkAgg(fig1, master=window)
    canvas1.draw()
    canvas1.get_tk_widget().pack()

    # Bar chart for Payment mode
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    df['Payment mode'].value_counts().plot(kind='bar', color='skyblue', ax=ax2)
    ax2.set_title("Transactions by Payment Mode")
    ax2.set_xlabel("Payment Mode")
    ax2.set_ylabel("Count")
    canvas2 = FigureCanvasTkAgg(fig2, master=window)
    canvas2.draw()
    canvas2.get_tk_widget().pack()

    # Anomalies (highlighted if any)
    anomalies = df[df['Is_Anomaly']]
    if not anomalies.empty:
        fig3, ax3 = plt.subplots(figsize=(5, 3))
        ax3.scatter(df.index, df['Amount'], label='All Transactions', alpha=0.6)
        ax3.scatter(anomalies.index, anomalies['Amount'], color='red', label='Anomalies')
        ax3.set_title("Anomaly Detection (Z-Score Based)")
        ax3.legend()
        canvas3 = FigureCanvasTkAgg(fig3, master=window)
        canvas3.draw()
        canvas3.get_tk_widget().pack()
    else:
        tk.Label(window, text="✅ No anomalies detected", fg="green").pack(pady=10)

    # Close Button
    tk.Button(window, text="Close", command=window.destroy, bg="red", fg="white").pack(pady=10)
