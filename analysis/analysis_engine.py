from scipy.stats import zscore
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def perform_clustering(df, n_clusters=4):
    df_cluster = df.copy()
    df_cluster['Hour'] = pd.to_datetime(df_cluster['Time'], format="%H:%M", errors='coerce').dt.hour.fillna(0)
    df_cluster['Is_Debit'] = df_cluster['Type'].apply(lambda x: 1 if x.lower() == 'debit' else 0)

    features = df_cluster[['Amount', 'Hour', 'Is_Debit']]
    scaled_features = StandardScaler().fit_transform(features)

    if len(df_cluster) < n_clusters:
        df_cluster['Cluster'] = 0
    else:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        df_cluster['Cluster'] = kmeans.fit_predict(scaled_features)

    return df_cluster

def detect_anomalies(df, z_threshold=2.5):
    df_anomaly = df.copy()
    df_anomaly['Z_Score'] = zscore(df_anomaly['Amount'])
    df_anomaly['Is_Anomaly'] = df_anomaly['Z_Score'].abs() > z_threshold
    return df_anomaly
