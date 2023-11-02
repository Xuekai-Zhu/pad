def solution():
    """A company was contracted to construct three buildings, with the second building being two times as tall as the first building. The third building had to be three times as tall as the combined height of the first and second buildings. If the first building was 600 feet, calculate the total height of the three buildings together."""
    # Define the height of the first building
    first_building = 600

    # Calculate the height of the second building
    second_building = 2 * first_building

    # Calculate the combined height of the first and second buildings
    total_height = first_building + second_building

    # Calculate the height of the third building
    third_building = 3 * total_height

    # Calculate the total height of the three buildings together
    total_height = first_building + second_building + third_building

    # Return the result
    result = total_height
    return result

print(solution())