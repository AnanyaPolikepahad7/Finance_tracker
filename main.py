# from ingestion.data_ingestion import load_and_clean_data
# from analysis.analysis_engine import perform_clustering, detect_anomalies
# from visualization.visualizer import plot_pie_chart_by_category, plot_bar_chart_by_category, plot_anomalies
# from ui.ui_app import launch_ui

# def run_analysis_for_user(user_id):
#     df = load_and_clean_data("data/transactions.csv")
#     df.columns = df.columns.str.strip()  # ✅ Strip whitespaces from column names
#     print("🧾 Columns loaded:", df.columns.tolist())

#     # Convert user_id to string for safe comparison
#     df = df[df['User_ID'].astype(str) == str(user_id)]
#     if df.empty:
#         print(f"No transactions found for user: {user_id}")
#         return

#     clustered_df = perform_clustering(df)
#     anomaly_df = detect_anomalies(clustered_df)

#     plot_pie_chart_by_category(anomaly_df)
#     plot_bar_chart_by_category(anomaly_df)
#     plot_anomalies(anomaly_df)

# if __name__ == "__main__":
#     launch_ui()

# main.py

from ui.ui_app import launch_ui

if __name__ == "__main__":
    launch_ui()
