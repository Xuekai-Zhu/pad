def solution():
    # Calculate total number of s'mores needed
    total_smores = 15 * 2

    # Calculate total number of bars needed
    bars_needed = total_smores / 3

    # Calculate total cost of bars
    cost = bars_needed * 1.5

    result = cost
    return result

print(solution())