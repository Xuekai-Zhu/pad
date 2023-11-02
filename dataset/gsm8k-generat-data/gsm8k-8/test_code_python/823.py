def solution():
    # Define the initial number of apples
    initial_apples = 74

    # Define the number of apples Ricki removes
    ricki_removes = 14

    # Define the number of apples Samson removes
    samson_removes = 2 * ricki_removes

    # Calculate the total number of apples removed
    total_removed = ricki_removes + samson_removes

    # Calculate the number of apples left in the basket
    apples_left = initial_apples - total_removed

    result = apples_left
    return result

print(solution())