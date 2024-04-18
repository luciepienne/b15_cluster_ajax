import pandas as pd
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import requests
import os


# # Get the absolute path to the 'data' directory
# data_dir = os.path.join(os.path.dirname(__file__), "data")
# # Specify the file name
# csv_filename = "Mall_Customers.csv"


# # Construct the absolute path to the CSV file
# csv_path = os.path.join(data_dir, csv_filename)
# create data repository if not exist
def fetch_normalize_and_read_rawdata():
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Path to the CSV file in the data directory
    csv_file_path = "data/Mall_Customers.csv"

    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        # If the file doesn't exist, download it from the URL
        url = "https://gist.githubusercontent.com/pravalliyaram/5c05f43d2351249927b8a3f3cc3e5ecf/raw/8bd6144a87988213693754baaa13fb204933282d/Mall_Customers.csv"
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Write the content to the CSV file
            with open(csv_file_path, "wb") as f:
                f.write(response.content)
        else:
            raise Exception(f"Failed to download CSV file from {url}")

        # Read the CSV file directly
    data = pd.read_csv(csv_file_path)
    # Rename columns
    data = data.rename(
        columns={
            "CustomerID": "customer_ID",
            "Gender": "gender",
            "Age": "age",
            "Annual Income (k$)": "annual_income",
            "Spending Score (1-100)": "spending_score",
        }
    )
    # Map gender to 0 and 1
    data["gender"] = data["gender"].map({"Male": 0, "Female": 1})
    feature_columns = ["age", "gender", "annual_income", "spending_score"]
    # to standardize the numerical features in other columns
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(data[feature_columns])
    return features_scaled


features_scaled = fetch_normalize_and_read_rawdata()


def kmeans_clustering(k, n_init):
    # Entraînement du modèle DBSCAN
    kmeans = KMeans(n_clusters=k, n_init=n_init, random_state=42)
    kmeans.fit(features_scaled)
    # Calcul du score de silhouette
    silhouette_score_kmeans = silhouette_score(features_scaled, kmeans.labels_)
    return silhouette_score_kmeans


def dbscan_clustering(eps, min_samples):
    # Entraînement du modèle DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(features_scaled)
    # Calcul du score de silhouette (bien que la silhouette ne soit pas le meilleur score pour DBSCAN)
    silhouette_score_dbscan = silhouette_score(features_scaled, dbscan.labels_)
    return silhouette_score_dbscan


def hierarchical_clustering(n_clusters, linkage):
    # Entraînement du modèle de clustering hiérarchique
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    hc.fit(features_scaled)
    # Calcul du score de silhouette
    silhouette_score_hc = silhouette_score(features_scaled, hc.labels_)
    return silhouette_score_hc
