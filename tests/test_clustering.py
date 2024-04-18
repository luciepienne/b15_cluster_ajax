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
    # Call the function
    features_scaled = fetch_normalize_and_read_rawdata()
    # Check if the returned features have a correct shape
    assert features_scaled.shape >= (
        150,
        4,
    )
    # # Check if all values in the gender column are between 0 and 1
    # assert np.all(np.logical_and(features_scaled[:, 1] >= 0, features_scaled[:, 1] <= 1))
    # # Check if the gender column contains only 0 or 1
    # assert np.all((features_scaled[:, 1] == 0) | (features_scaled[:, 1] == 1))


test_fetch_normalize_and_read_rawdata()


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
