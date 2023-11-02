def solution():
    
    middle_building_height = 100
    left_building_height = 0.8 * middle_building_height
    right_building_height = (left_building_height + middle_building_height) - 20
    total_height = left_building_height + middle_building_height + right_building_height
    result = total_height
    return result

print(solution())