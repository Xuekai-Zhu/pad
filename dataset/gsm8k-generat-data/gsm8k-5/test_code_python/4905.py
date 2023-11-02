def solution():
    total_capacity = 100  # Total capacity of the jar
    capacity_used = 20 * 2 + 40 * 1  # Capacity used by the toenails already collected
    remaining_capacity = total_capacity - capacity_used  # Remaining capacity of the jar

    # Calculate the number of regular toenails that can be fit in the remaining capacity
    regular_toenail_capacity = remaining_capacity / 2
    result = regular_toenail_capacity
    return result

print(solution())