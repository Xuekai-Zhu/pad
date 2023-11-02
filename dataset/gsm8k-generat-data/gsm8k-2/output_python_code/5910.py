def solution():
    """A building has 20 floors. Each floor is 3 meters high, except for the last two floors. The last two floors are each 0.5 meters higher. How tall is the building?"""
    standard_floor_height = 3
    last_two_floor_height = 3 + 0.5
    num_standard_floors = 18
    total_standard_floor_height = num_standard_floors * standard_floor_height
    total_last_two_floor_height = 2 * last_two_floor_height
    total_building_height = total_standard_floor_height + total_last_two_floor_height
    result = total_building_height
    return result

print(solution())