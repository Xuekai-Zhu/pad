def solution():
    # Calculate the area of each wall
    area_wall1 = 3 * 2  # width 3m, height 2m
    area_wall2 = 3 * 2  # width 3m, height 2m
    area_wall3 = 5 * 2  # width 5m, height 2m
    area_wall4 = 4 * 2  # width 4m, height 2m

    # Calculate the total area to be painted
    total_area = area_wall1 + area_wall2 + area_wall3 + area_wall4

    # Calculate the number of cans of paint needed
    cans_of_paint = total_area / 2  # Each can covers 2 square meters

    result = cans_of_paint
    return result

print(solution())