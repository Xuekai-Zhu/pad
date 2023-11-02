def solution():
    # Calculate the area of the floor
    floor_area = 10 * 8

    # Calculate the area of the carpet
    carpet_area = 4 * 4

    # Calculate the number of carpets needed to cover the floor
    carpets_needed = floor_area / (4 * 4)

    # Calculate the area of the uncovered portion of the floor
    uncovered_area = floor_area - (carpets_needed * carpet_area)

    result = uncovered_area
    return result

print(solution())