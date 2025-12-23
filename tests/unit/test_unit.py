import pytest
from app.routes import tutor

@pytest.mark.unit
def test_explain_unit():
    result = tutor.explain({"prompt": "AI"})
    assert "AI" in result["response"]