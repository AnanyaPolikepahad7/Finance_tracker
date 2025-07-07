import pandas as pd
from ingestion.data_ingestion import load_and_clean_data
from analysis.analysis_engine import perform_clustering, detect_anomalies
from visualization.visualizer import show_visualizations

def run_analysis_for_user(user_id):
    df = load_and_clean_data("data/transactions.csv")

    # Normalize User_ID values to remove decimal points
    df['User_ID'] = df['User_ID'].astype(str).str.strip().str.replace('.0', '', regex=False)
    user_id = str(user_id).strip().replace('.0', '')

    print(f"📥 All User_IDs: {df['User_ID'].unique()}")
    print(f"🔎 Filtering for User_ID: {user_id}")

    user_df = df[df['User_ID'] == user_id]

    if user_df.empty:
        print(f"🚫 No transactions found for user: {user_id}")
        return

    print(f"🔍 Transactions found for user {user_id}: {len(user_df)}")

    clustered_df = perform_clustering(user_df)
    final_df = detect_anomalies(clustered_df)

    show_visualizations(final_df, user_id)
