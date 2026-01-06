import pytest

from tiny_python_utils.env_loader import load_required_env_vars



def test_load_required_env_vars_success(monkeypatch):
    monkeypatch.setenv("TEST_VAR", "value")

    result = load_required_env_vars(["TEST_VAR"])

    assert result == {"TEST_VAR": "value"}


def test_multiple_env_vars(monkeypatch):
    monkeypatch.setenv("VAR_ONE", "1")
    monkeypatch.setenv("VAR_TWO", "2")

    result = load_required_env_vars(["VAR_ONE", "VAR_TWO"])

    assert result == {"VAR_ONE": "1", "VAR_TWO": "2"}


def test_missing_env_var_raises_error(monkeypatch):
    monkeypatch.delenv("MISSING_VAR", raising=False)

    with pytest.raises(EnvironmentError) as exc:
        load_required_env_vars(["MISSING_VAR"])

    assert "MISSING_VAR" in str(exc.value)
