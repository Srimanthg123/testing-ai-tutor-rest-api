import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.integration
def test_personalize_endpoint():
    response = client.post(
        "/personalize",
        json={"prompt": "AI", "level": "beginner"}
    )
    assert response.status_code == 200