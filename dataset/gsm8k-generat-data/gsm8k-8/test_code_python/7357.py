def solution():
    # Calculate the area of the rectangular patch
    rectangular_area = 6 * 7

    # Calculate the area of the square patch
    square_area = 5 * 5

    # Calculate the total area to be filled
    total_area = rectangular_area + square_area

    # Calculate the total amount of sand needed in grams
    sand_needed = total_area * 3

    result = sand_needed
    return result

print(solution())