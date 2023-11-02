def solution():
    total_capacity = 16  # The USB drive has a capacity of 16 GB
    busy_capacity = 0.5 * total_capacity  # 50% of the capacity is already busy

    # Calculate the available capacity
    available_capacity = total_capacity - busy_capacity
    result = available_capacity
    return result

print(solution())