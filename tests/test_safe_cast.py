from tiny_python_utils.safe_cast import safe_cast


def test_safe_cast_success():
    assert safe_cast("123", int) == 123
    assert safe_cast("3.14", float) == 3.14


def test_safe_cast_failure_returns_default():
    assert safe_cast("abc", int, default=0) == 0
    assert safe_cast(None, int, default=-1) == -1


def test_safe_cast_failure_returns_none_by_default():
    assert safe_cast("abc", int) is None
