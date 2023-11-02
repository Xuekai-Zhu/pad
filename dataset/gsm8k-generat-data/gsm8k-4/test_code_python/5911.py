def solution():
    """A building has 20 floors. Each floor is 3 meters high, except for the last two floors. The last two floors are each 0.5 meters higher. How tall is the building?"""
    # Calculate the height of the first 18 floors
    standard_floor_height = 3
    standard_floor_count = 18
    standard_floor_total_height = standard_floor_height * standard_floor_count

    # Calculate the height of the last two floors
    last_floor_height = 3 + 0.5
    last_floor_count = 2
    last_floor_total_height = last_floor_height * last_floor_count

    # Calculate the total height of the building
    total_height = standard_floor_total_height + last_floor_total_height

    # return the result
    result = total_height
    return result

print(solution())