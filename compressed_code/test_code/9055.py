def solution():
    
    middle_building = 100
    left_building = middle_building * 0.8
    right_building = (middle_building + left_building) - 20
    total_height = middle_building + left_building + right_building
    result = total_height
    return result

print(solution())