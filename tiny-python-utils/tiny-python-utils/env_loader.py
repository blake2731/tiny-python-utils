import os
from typing import Iterable


def load_required_env_vars(required_vars: Iterable[str]) -> dict:
    """
    Load and validate required environment variables.

    Raises:
        EnvironmentError: if any required variable is missing
    """
    missing = []
    values = {}

    for var in required_vars:
        value = os.getenv(var)
        if value is None:
            missing.append(var)
        else:
            values[var] = value

    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    return values


if __name__ == "__main__":
    # Example usage
    config = load_required_env_vars(["HOME", "PATH"])
    print(config)
