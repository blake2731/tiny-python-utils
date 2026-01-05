def human_readable_time(seconds: int) -> str:
    """
    Convert seconds into a human-readable time string.
    Example: 3661 -> '1h 1m 1s'
    """
    if seconds < 0:
        raise ValueError("Seconds must be non-negative")

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    parts = []
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if secs or not parts:
        parts.append(f"{secs}s")

    return " ".join(parts)


if __name__ == "__main__":
    print(human_readable_time(3661))
