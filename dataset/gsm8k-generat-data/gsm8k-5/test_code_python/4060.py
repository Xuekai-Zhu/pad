def solution():
    playground_area = 12**2  # Area of the square playground
    building_area = 8 * 5  # Area of the maintenance building

    # Calculate the area of the playground not covered by the maintenance building
    uncovered_area = playground_area - building_area
    result = uncovered_area
    return result

print(solution())