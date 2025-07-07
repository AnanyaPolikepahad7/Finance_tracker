# visualization/visualizer.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_pie_chart_by_category(df, tk_frame=None):
    category_sums = df.groupby('Category')['Amount'].sum()
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(category_sums, labels=category_sums.index, autopct='%1.1f%%')
    ax.set_title('Spending by Category')

    if tk_frame:
        canvas = FigureCanvasTkAgg(fig, master=tk_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    else:
        plt.show()

def plot_bar_chart_by_category(df, tk_frame=None):
    category_sums = df.groupby('Category')['Amount'].sum()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(category_sums.index, category_sums.values)
    ax.set_title('Total Spend per Category')
    ax.set_ylabel('Amount')
    plt.xticks(rotation=45)

    if tk_frame:
        canvas = FigureCanvasTkAgg(fig, master=tk_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    else:
        plt.show()

def plot_anomalies(df, tk_frame=None):
    anomaly_points = df[df['Is_Anomaly']]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df['Amount'], label='All Transactions')
    ax.scatter(anomaly_points.index, anomaly_points['Amount'], color='red', label='Anomalies')
    ax.set_title('Anomaly Detection')
    ax.legend()

    if tk_frame:
        canvas = FigureCanvasTkAgg(fig, master=tk_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    else:
        plt.show()
