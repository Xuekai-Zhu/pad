def solution():
    # Calculate the total number of apples picked in the first 30 days
    total_apples_picked = 30 * 4

    # Calculate the total number of apples in the orchard before the last collection
    total_apples_before_last_collection = total_apples_picked + 230

    # Calculate the total number of apples collected including the last collection
    total_apples_collected = total_apples_before_last_collection + 4

    result = total_apples_collected
    return result

print(solution())