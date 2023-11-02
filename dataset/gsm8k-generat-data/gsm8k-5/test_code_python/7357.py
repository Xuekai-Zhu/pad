def solution():
    # Calculate the area of the rectangular patch
    area_rectangular = 6 * 7

    # Calculate the area of the square patch
    area_square = 5 * 5

    # Calculate the total area to be filled with sand
    total_area = area_rectangular + area_square

    # Calculate the total number of grams of sand needed
    sand_needed = total_area * 3
    result = sand_needed
    return result

print(solution())