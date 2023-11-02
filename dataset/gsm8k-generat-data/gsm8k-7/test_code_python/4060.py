def solution():
    playground_side_length = 12
    building_length = 8
    building_width = 5

    # Calculate the area of the maintenance building
    building_area = building_length * building_width

    # Calculate the area of the whole playground
    playground_area = playground_side_length ** 2

    # Calculate the area of the playground not covered by the maintenance building
    uncovered_area = playground_area - building_area
    result = uncovered_area
    return result

print(solution())