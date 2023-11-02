def solution():
    # Calculate the combined weight of the three adults and two children
    total_weight = 3 * 140 + 2 * 64  

    # Calculate the maximum weight of the next person to get in the elevator
    remaining_weight = 600 - total_weight
    result = remaining_weight
    return result

print(solution())