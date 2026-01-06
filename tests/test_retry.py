import pytest

from retry import retry


def test_retry_succeeds_after_failure():
    calls = {"count": 0}

    def flaky():
        calls["count"] += 1
        if calls["count"] < 2:
            raise ValueError("Temporary failure")
        return "success"

    result = retry(flaky, attempts=3, delay=0)

    assert result == "success"
    assert calls["count"] == 2


def test_retry_raises_after_exhausting_attempts():
    def always_fails():
        raise RuntimeError("Nope")

    with pytest.raises(RuntimeError):
        retry(always_fails, attempts=2, delay=0)
