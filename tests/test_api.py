"""Tests for the FastAPI recommendation service."""

from fastapi.testclient import TestClient
from service.app import app

client = TestClient(app)


def test_healthz():
    """Test health endpoint returns OK."""
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "model_version" in data


def test_recommend_default():
    """Test default recommendation (k=20)."""
    response = client.get("/recommend/1")
    assert response.status_code == 200
    ids = response.text.strip('"').split(",")
    assert len(ids) == 20
    assert all(id_.isdigit() for id_ in ids)


def test_recommend_custom_k():
    """Test recommendation with custom k."""
    response = client.get("/recommend/1?k=5")
    assert response.status_code == 200
    ids = response.text.strip('"').split(",")
    assert len(ids) == 5


def test_metrics_endpoint():
    """Test Prometheus metrics endpoint."""
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "recommend_requests_total" in response.text


def test_switch_unauthorized():
    """Test that switch without token is rejected."""
    response = client.post("/switch?model=v2.0")
    assert response.status_code == 403
