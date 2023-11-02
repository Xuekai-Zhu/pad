def solution():
    first_building = 600
    second_building = first_building * 2
    third_building = (first_building + second_building) * 3
    total_height = first_building + second_building + third_building
    result = total_height
    return result

print(solution())