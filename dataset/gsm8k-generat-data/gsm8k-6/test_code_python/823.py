def solution():
    # Calculate the total number of apples removed
    total_removed = 14 + 2*14  # Samson removes twice as many as Ricki
    remaining_apples = 74 - total_removed  # Calculate the remaining number of apples
    result = remaining_apples
    return result

print(solution())