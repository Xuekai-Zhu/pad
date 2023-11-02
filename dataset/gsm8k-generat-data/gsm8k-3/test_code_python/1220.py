def solution():
    """A company was contracted to construct three buildings, with the second building being two times as tall as the first building. The third building had to be three times as tall as the combined height of the first and second buildings. If the first building was 600 feet, calculate the total height of the three buildings together."""
    # Define the height of the first building
    height_1 = 600

    # Calculate the height of the second building
    height_2 = height_1 * 2

    # Calculate the combined height of the first two buildings
    combined_height = height_1 + height_2

    # Calculate the height of the third building
    height_3 = combined_height * 3

    # Calculate the total height of the three buildings together
    total_height = height_1 + height_2 + height_3

    # Display the total height
    result = total_height
    return result

print(solution())