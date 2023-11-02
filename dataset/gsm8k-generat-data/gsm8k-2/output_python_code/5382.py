def solution():
    """A wood stove burns 4 bundles of wood in the morning, then some more in the afternoon. If there were 10 bundles of wood at the start of the day and 3 bundles of wood at the end of the day, how many bundles of wood were burned in the afternoon?"""
    morning_burn = 4
    start_of_day = 10
    end_of_day = 3
    afternoon_burn = start_of_day - morning_burn - end_of_day
    result = afternoon_burn
    return result

print(solution())