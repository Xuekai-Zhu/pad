def solution():
    # Calculate the area of each wall
    area_wall1 = 3 * 2
    area_wall2 = 3 * 2
    area_wall3 = 5 * 2
    area_wall4 = 4 * 2

    # Calculate the total area to be painted
    total_area = area_wall1 + area_wall2 + area_wall3 + area_wall4

    # Calculate the number of cans needed
    cans_needed = total_area / 2
    result = cans_needed
    return result

print(solution())