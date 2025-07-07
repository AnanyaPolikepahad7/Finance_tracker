from scipy.stats import zscore
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def perform_clustering(df, n_clusters=4):
    # Create a working copy
    df_cluster = df.copy()

    # Extract hour of transaction from time
    df_cluster['Hour'] = pd.to_datetime(df_cluster['Time'], format="%H:%M", errors='coerce').dt.hour
    df_cluster['Hour'] = df_cluster['Hour'].fillna(0)

    # Encode 'Type' as binary: Debit = 1, Credit = 0
    df_cluster['Is_Debit'] = df_cluster['Type'].apply(lambda x: 1 if x.lower() == 'debit' else 0)

    # Feature set
    features = df_cluster[['Amount', 'Hour', 'Is_Debit']]

    # Scale features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Ensure we have enough samples for the number of clusters
    if df_cluster.shape[0] < n_clusters:
        print(f"⚠️ Not enough transactions for clustering. Found only {df_cluster.shape[0]} transactions.")
        df_cluster['Cluster'] = -1  # Assign a dummy cluster label
        return df_cluster

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df_cluster['Cluster'] = kmeans.fit_predict(scaled_features)

    return df_cluster

def detect_anomalies(df, z_threshold=2.5):
    df_anomaly = df.copy()

    # Compute z-scores for the Amount column
    df_anomaly['Z_Score'] = zscore(df_anomaly['Amount'])

    # Flag anomalies
    df_anomaly['Is_Anomaly'] = df_anomaly['Z_Score'].abs() > z_threshold

    return df_anomaly
