def solution():
    first_building = 600
    second_building = 2 * first_building
    third_building = 3 * (first_building + second_building)
    total_height = first_building + second_building + third_building
    result = total_height
    return result

print(solution())