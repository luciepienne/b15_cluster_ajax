from fastapi.testclient import TestClient
import os
import sys

# Append the parent directory of the 'tests' directory to sys.path
tests_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(tests_dir)
sys.path.append(project_dir)

from back.api_models import app

client = TestClient(app)


def test_kmeans_endpoint():
    resp = client.get("/kmeans")
    assert resp.status_code == 200
    assert isinstance(resp.json(), float)


def test_dbscan_endpoint():
    resp = client.get("/dbscan")
    assert resp.status_code == 200
    assert isinstance(resp.json(), float)


def test_hierarchical_endpoint():
    resp = client.get("/hierarchical")
    assert resp.status_code == 200
    assert isinstance(resp.json(), float)
