def solution():
    # Area of the rectangular sail
    area_rectangular_sail = 5 * 8

    # Area of the first right triangular sail
    base1 = 3
    height1 = 4
    area_triangular_sail1 = (base1 * height1) / 2

    # Area of the second right triangular sail
    base2 = 4
    height2 = 6
    area_triangular_sail2 = (base2 * height2) / 2

    # Total area of canvas needed
    total_area = area_rectangular_sail + area_triangular_sail1 + area_triangular_sail2
    result = total_area
    return result

print(solution())