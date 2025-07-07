# runner/analyzer_runner.py

from ingestion.data_ingestion import load_and_clean_data
from analysis.analysis_engine import perform_clustering, detect_anomalies
from visualization.visualizer import (
    plot_pie_chart_by_category, plot_bar_chart_by_category, plot_anomalies
)

def run_analysis_for_user(user_id, tk_frame=None):
    df = load_and_clean_data("data/transactions.csv")
    print("🔍 All available User_IDs:", df['User_ID'].unique())
    df.columns = df.columns.str.strip()
    df['User_ID'] = df['User_ID'].astype(str).str.replace('.0', '', regex=False)
    df = df[df['User_ID'] == str(user_id)]



    if df.empty:
        print(f"No transactions found for user: {user_id}")
        return

    clustered_df = perform_clustering(df)
    anomaly_df = detect_anomalies(clustered_df)

    plot_pie_chart_by_category(anomaly_df, tk_frame)
    plot_bar_chart_by_category(anomaly_df, tk_frame)
    plot_anomalies(anomaly_df, tk_frame)
