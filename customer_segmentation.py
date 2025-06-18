import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Load the data
df = pd.read_csv('customer_data_records (1).csv')

# Select features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Find the optimal number of clusters using the elbow method
inertias = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(K, inertias, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.savefig('elbow_curve.png')
plt.close()

# Perform K-means clustering with 5 clusters (based on elbow method)
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Create a scatter plot of the clusters
plt.figure(figsize=(12, 8))
scatter = plt.scatter(df['Annual Income (k$)'], 
                     df['Spending Score (1-100)'], 
                     c=df['Cluster'], 
                     cmap='viridis')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segments')
plt.colorbar(scatter, label='Cluster')
plt.savefig('customer_segments.png')
plt.close()

# Analyze cluster characteristics
cluster_analysis = df.groupby('Cluster').agg({
    'Annual Income (k$)': ['mean', 'std', 'min', 'max'],
    'Spending Score (1-100)': ['mean', 'std', 'min', 'max'],
    'CustomerID': 'count'
}).round(2)

# Save cluster analysis to CSV
cluster_analysis.to_csv('cluster_analysis.csv')

# Print cluster analysis
print("\nCluster Analysis:")
print(cluster_analysis)

# Create a heatmap of cluster centers
cluster_centers = pd.DataFrame(
    scaler.inverse_transform(kmeans.cluster_centers_),
    columns=['Annual Income (k$)', 'Spending Score (1-100)']
)

plt.figure(figsize=(10, 6))
sns.heatmap(cluster_centers, annot=True, cmap='YlOrRd', fmt='.2f')
plt.title('Cluster Centers')
plt.savefig('cluster_centers.png')
plt.close() 