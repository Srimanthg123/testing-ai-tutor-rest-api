import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.integration
def test_stream_endpoint():
    response = client.post("/stream", json={"prompt": "AI"})
    assert response.status_code == 200