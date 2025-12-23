import pytest
from app.services import local_llm


@pytest.mark.unit
def test_explain_with_local_llm(monkeypatch):
    # Mock function
    def mock_local_generate(prompt):
        return "Mocked local LLM response"

    # Patch the real function
    monkeypatch.setattr(
        "app.services.local_llm.local_generate",
        mock_local_generate
    )

    # Call the function under test
    result = local_llm.local_generate("Explain AI")

    # Assertion
    assert "Mocked" in result