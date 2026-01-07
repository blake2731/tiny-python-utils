from typing import Any, Callable, TypeVar

T = TypeVar("T")


def safe_cast(value: Any, cast: Callable[[Any], T], default: T | None = None) -> T | None:
    """
    Safely cast a value to a given type.

    Args:
        value: The value to cast
        cast: A callable (e.g., int, float, str)
        default: Value to return if casting fails

    Returns:
        The cast value, or default if casting fails
    """
    try:
        return cast(value)
    except (TypeError, ValueError):
        return default
