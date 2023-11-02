def solution():
    """A company was contracted to construct three buildings, with the second building being two times as tall as the first building. The third building had to be three times as tall as the combined height of the first and second buildings. If the first building was 600 feet, calculate the total height of the three buildings together."""
    first_building_height = 600
    second_building_height = 2 * first_building_height
    combined_height = first_building_height + second_building_height
    third_building_height = 3 * combined_height
    total_height = first_building_height + second_building_height + third_building_height
    result = total_height
    return result

print(solution())