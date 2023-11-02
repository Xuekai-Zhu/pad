def solution():
    # Calculate the area of glass needed for each wall
    area_wall1 = 30 * 12
    area_wall2 = 30 * 12
    area_wall3 = 20 * 12

    # Calculate the total area of glass needed
    total_area = 2 * (area_wall1 + area_wall2) + area_wall3

    result = total_area
    return result

print(solution())