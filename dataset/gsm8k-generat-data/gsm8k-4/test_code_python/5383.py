def solution():
    """A wood stove burns 4 bundles of wood in the morning, then some more in the afternoon. If there were 10 bundles of wood at the start of the day and 3 bundles of wood at the end of the day, how many bundles of wood were burned in the afternoon?"""
    # Define the total number of bundles of wood
    total_bundles = 10

    # Define the number of bundles burned in the morning
    morning_bundles = 4

    # Define the number of bundles remaining after morning burn
    remaining_bundles = total_bundles - morning_bundles

    # Define the number of bundles burned in the afternoon
    afternoon_bundles = remaining_bundles - 3

    # return the result
    result = afternoon_bundles
    return result

print(solution())