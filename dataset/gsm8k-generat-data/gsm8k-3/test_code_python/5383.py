def solution():
    """A wood stove burns 4 bundles of wood in the morning, then some more in the afternoon. If there were 10 bundles of wood at the start of the day and 3 bundles of wood at the end of the day, how many bundles of wood were burned in the afternoon?"""
    # Define the number of bundles burned in the morning and the final number of bundles
    MORNING_BURN = 4
    FINAL_BUNDLES = 3

    # Define the initial number of bundles and the number burned in the afternoon
    initial_bundles = 10
    afternoon_burn = initial_bundles - MORNING_BURN - FINAL_BUNDLES

    # Display the number of bundles burned in the afternoon
    result = afternoon_burn
    return result

print(solution())