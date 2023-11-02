def solution():
    # Find the height of the second building
    second_building = 2 * 600

    # Find the combined height of the first and second building
    combined_height = 600 + second_building

    # Find the height of the third building
    third_building = 3 * combined_height

    # Calculate the total height of the three buildings
    total_height = 600 + second_building + third_building
    result = total_height
    return result

print(solution())