def solution():
    # Calculate the area of the maintenance building
    maintenance_area = 8 * 5

    # Calculate the area of the playground
    playground_area = 12 ** 2

    # Calculate the area not covered by the maintenance building
    not_covered_area = playground_area - maintenance_area
    result = not_covered_area
    return result

print(solution())