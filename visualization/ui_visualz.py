import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from visualization.visualizer import plot_pie_chart_by_category, plot_pie_chart_by_account, plot_anomalies

def show_visualizations(df, user_id):
    window = tk.Toplevel()
    window.title(f"📊 Finance Insights for User {user_id}")
    window.geometry("1000x900")

    title = tk.Label(window, text=f"📊 Spending Analysis for User {user_id}", font=("Arial", 16))
    title.pack(pady=10)

    tabs = ttk.Notebook(window)
    pie_tab = ttk.Frame(tabs)
    account_tab = ttk.Frame(tabs)
    anomaly_tab = ttk.Frame(tabs)

    tabs.add(pie_tab, text="By Category")
    tabs.add(account_tab, text="By Account")
    tabs.add(anomaly_tab, text="Anomalies")
    tabs.pack(expand=1, fill="both")

    # Embedding Matplotlib plots
    for tab, plot_func in zip([pie_tab, account_tab, anomaly_tab],
                              [plot_pie_chart_by_category, plot_pie_chart_by_account, plot_anomalies]):
        fig = plot_func(df, return_fig=True)
        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    window.mainloop()
