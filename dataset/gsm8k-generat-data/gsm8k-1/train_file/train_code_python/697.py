def solution():
    """On a 16 GB (gigabyte) capacity USB drive, 50% is already busy. Calculate the number of gigabytes still available."""
    total_capacity = 16
    busy_capacity_percent = 50
    available_capacity_percent = 100 - busy_capacity_percent
    available_capacity = (available_capacity_percent / 100) * total_capacity
    result = available_capacity
    return result

print(solution())