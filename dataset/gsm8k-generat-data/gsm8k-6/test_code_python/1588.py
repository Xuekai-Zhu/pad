def solution():
    # Calculate the area of the rectangular sail
    area_rectangular_sail = 5 * 8

    # Calculate the area of the first triangular sail
    area_triangular_sail_1 = (3 * 4) / 2

    # Calculate the area of the second triangular sail
    area_triangular_sail_2 = (4 * 6) / 2

    # Calculate the total area of canvas needed
    total_canvas_area = area_rectangular_sail + area_triangular_sail_1 + area_triangular_sail_2
    result = total_canvas_area
    return result

print(solution())