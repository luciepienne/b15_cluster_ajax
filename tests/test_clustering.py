from unittest.mock import patch
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "back")))

from functions_models import (
    kmeans_clustering,
    dbscan_clustering,
    hierarchical_clustering,
    fetch_normalize_and_read_rawdata,
)


def test_fetch_normalize_and_read_rawdata():
    # Mock requests.get to return test CSV content
    with patch("requests.get") as mock_get:
        # Prepare test data (sample CSV content)
        test_csv_content = (
            "CustomerID,Gender,Age,Annual Income (k$),Spending Score (1-100)\n"
            "1,Male,19,15,39\n"
            "2,Female,21,15,81\n"
            "3,Female,20,16,6\n"
            # Add more rows as needed
        )

        mock_get.return_value.status_code = 200
        mock_get.return_value.content = test_csv_content.encode("utf-8")

        # Call the function
        features_scaled = fetch_normalize_and_read_rawdata()

    # Check if the returned features have the correct shape
    assert features_scaled.shape == (
        3,
        4,
    )  # Assuming 3 rows and 4 columns in the test CSV


# Test KMeans clustering function
def test_kmeans_clustering():
    k = 5
    n_init = 10
    silhouette_score = kmeans_clustering(k, n_init)
    assert 0 <= silhouette_score <= 10


# Test DBSCAN clustering function
def test_dbscan_clustering():
    eps = 0.5
    min_samples = 5
    silhouette_score = dbscan_clustering(eps, min_samples)
    assert 0 <= silhouette_score <= 10


# Test Hierarchical clustering function
def test_hierarchical_clustering():
    n_clusters = 3
    linkage = "ward"
    silhouette_score = hierarchical_clustering(n_clusters, linkage)
    assert 0 <= silhouette_score <= 10


test_dbscan_clustering()
