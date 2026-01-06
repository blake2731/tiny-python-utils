import time
from typing import Callable, Type, Tuple


def retry(
    func: Callable,
    attempts: int = 3,
    delay: float = 0.5,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
):
    """
    Retry a function if it raises specified exceptions.

    Args:
        func: Function to execute
        attempts: Number of attempts before giving up
        delay: Delay between attempts in seconds
        exceptions: Exceptions that trigger a retry
    """
    last_exception = None

    for attempt in range(attempts):
        try:
            return func()
        except exceptions as exc:
            last_exception = exc
            if attempt < attempts - 1:
                time.sleep(delay)

    raise last_exception
