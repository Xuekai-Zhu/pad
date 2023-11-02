def solution():
    # Calculate the current weight in the elevator
    current_weight = 3 * 140 + 2 * 64  # Three adults and two children

    # Calculate the maximum weight the elevator can hold
    max_weight = 600

    # Calculate the maximum weight of the next person to get in the elevator
    max_next_weight = max_weight - current_weight

    result = max_next_weight
    return result

print(solution())