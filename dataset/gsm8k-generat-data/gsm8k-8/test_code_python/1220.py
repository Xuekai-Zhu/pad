def solution():
    # Define the height of the first building
    first_building = 600

    # Define the height of the second building, which is two times as tall as the first building
    second_building = 2 * first_building

    # Define the height of the third building, which is three times as tall as the combined height of the first and second buildings
    third_building = 3 * (first_building + second_building)

    # Calculate the total height of the three buildings together
    total_height = first_building + second_building + third_building
    result = total_height
    return result

print(solution())