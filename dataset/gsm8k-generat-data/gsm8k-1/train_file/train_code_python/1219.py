def solution():
    """A company was contracted to construct three buildings, with the second building being two times as tall as the first building. The third building had to be three times as tall as the combined height of the first and second buildings. If the first building was 600 feet, calculate the total height of the three buildings together."""
    first_building = 600
    second_building = 2 * first_building
    third_building = 3 * (first_building + second_building)
    total_height = first_building + second_building + third_building
    result = total_height
    return result

print(solution())