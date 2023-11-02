def solution():
    total_capacity = 425
    num_levels = 5
    num_parked = 23

    # Calculate the total capacity of one level
    level_capacity = total_capacity / num_levels

    # Calculate how many more cars can fit on the level
    available_spots = level_capacity - num_parked
    result = available_spots
    return result

print(solution())