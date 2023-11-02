def solution():
    """A wood stove burns 4 bundles of wood in the morning, then some more in the afternoon. If there were 10 bundles of wood at the start of the day and 3 bundles of wood at the end of the day, how many bundles of wood were burned in the afternoon?"""
    morning_bundles = 4
    start_bundles = 10
    end_bundles = 3
    afternoon_bundles = start_bundles - morning_bundles - end_bundles
    result = afternoon_bundles
    return result

print(solution())