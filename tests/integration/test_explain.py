import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.integration
def test_explain_endpoint():
    response = client.post("/explain", json={"prompt": "AI"})
    assert response.status_code == 200