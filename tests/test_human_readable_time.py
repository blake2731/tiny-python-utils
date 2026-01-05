import pytest

from human_readable_time import human_readable_time


def test_seconds_only():
    assert human_readable_time(45) == "45s"


def test_minutes_and_seconds():
    assert human_readable_time(125) == "2m 5s"


def test_hours_minutes_seconds():
    assert human_readable_time(3661) == "1h 1m 1s"


def test_zero_seconds():
    assert human_readable_time(0) == "0s"


def test_negative_seconds_raises_error():
    with pytest.raises(ValueError):
        human_readable_time(-1)
