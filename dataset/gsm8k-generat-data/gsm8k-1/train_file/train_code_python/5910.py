def solution():
    """A building has 20 floors. Each floor is 3 meters high, except for the last two floors. The last two floors are each 0.5 meters higher. How tall is the building?"""
    normal_floor_height = 3
    last_two_floors_extra_height = 0.5 * 2
    total_height = (normal_floor_height * 18) + (last_two_floors_extra_height * 2)
    result = total_height
    return result

print(solution())