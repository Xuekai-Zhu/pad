def solution():
    # Calculate the total number of empty cans already collected
    total_collected = 30 + 43

    # Calculate the number of empty cans still needed
    cans_needed = 100 - total_collected
    result = cans_needed
    return result

print(solution())