def solution():
    
    standard_floor_height = 3
    last_two_floor_height = 3 + 0.5
    num_standard_floors = 18
    total_standard_floor_height = num_standard_floors * standard_floor_height
    total_last_two_floor_height = 2 * last_two_floor_height
    total_building_height = total_standard_floor_height + total_last_two_floor_height
    result = total_building_height
    return result

print(solution())