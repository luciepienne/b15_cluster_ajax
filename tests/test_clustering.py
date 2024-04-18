from back.functions_models import (
    kmeans_clustering,
    dbscan_clustering,
    hierarchical_clustering,
)
import pytest


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
