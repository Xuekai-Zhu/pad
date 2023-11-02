def solution():
    # Calculate the area of the rectangular sail
    rect_sail_area = 5 * 8

    # Calculate the area of the first right triangular sail
    tri_sail1_area = (3 * 4) / 2

    # Calculate the area of the second right triangular sail
    tri_sail2_area = (4 * 6) / 2

    # Calculate the total area of canvas needed
    total_area = rect_sail_area + tri_sail1_area + tri_sail2_area

    result = total_area
    return result

print(solution())