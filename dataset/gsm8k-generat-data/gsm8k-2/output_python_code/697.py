def solution():
    """On a 16 GB (gigabyte) capacity USB drive, 50% is already busy. Calculate the number of gigabytes still available."""
    total_capacity = 16
    busy_capacity = total_capacity * 0.5
    available_capacity = total_capacity - busy_capacity
    result = available_capacity
    return result

print(solution())