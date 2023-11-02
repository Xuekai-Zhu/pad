def solution():
    
    first_building_height = 600
    second_building_height = 2 * first_building_height
    combined_height = first_building_height + second_building_height
    third_building_height = 3 * combined_height
    total_height = first_building_height + second_building_height + third_building_height
    result = total_height
    return result

print(solution())