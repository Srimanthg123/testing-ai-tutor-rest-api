import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.integration
def test_explain_endpoint():
    payload = {
        "question": "What is AI?",
        "model_type": "local"
    }

    response = client.post("/tutor/explain", json=payload)

    assert response.status_code == 200
    assert "answer" in response.json()