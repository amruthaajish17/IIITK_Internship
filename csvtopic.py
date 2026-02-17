import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Step 1: Load Your CSV
# -------------------------
df = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\detailed_flows_output.csv")

print(df.columns)  # Always handy to double-check columns

# -------------------------
# Step 2: Select Relevant Features
# -------------------------
features = ['Packet Length', 'Relative Time']
df = df.dropna(subset=features)
X = df[features]

# -------------------------
# Step 3: KMeans Clustering
# -------------------------
kmeans = KMeans(n_clusters=2, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Packet Length', y='Relative Time', hue='cluster', palette='viridis')
plt.title("KMeans Clustering of Network Flows")
plt.tight_layout()
plt.savefig(r"C:\Users\hp\OneDrive\Desktop\kmeans_clustering_output.png")
plt.close()

# -------------------------
# Step 4: DBSCAN Clustering
# -------------------------
dbscan = DBSCAN(eps=500, min_samples=5)
df['dbscan_cluster'] = dbscan.fit_predict(X)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Packet Length', y='Relative Time', hue='dbscan_cluster', palette='Set2')
plt.title("DBSCAN Clustering")
plt.tight_layout()
plt.savefig(r"C:\Users\hp\OneDrive\Desktop\dbscan_clustering_output.png")
plt.close()

# -------------------------
# Step 5: Isolation Forest
# -------------------------
model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(X)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Packet Length', y='Relative Time', hue='anomaly', palette='coolwarm')
plt.title("Anomaly Detection (Isolation Forest)")
plt.tight_layout()
plt.savefig(r"C:\Users\hp\OneDrive\Desktop\isolation_forest_output.png")
plt.close()

# -------------------------
# Step 6: Save Final Labeled Dataset
# -------------------------
df.to_csv(r"C:\Users\hp\OneDrive\Desktop\labeled_network_data.csv", index=False)

print(" Done ! Files saved on your Desktop:")
print("- labeled_network_data.csv")
print("- kmeans_clustering_output.png")
print("- dbscan_clustering_output.png")
print("- isolation_forest_output.png")
