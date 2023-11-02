def solution():
    rect_sail_area = 5 * 8

    # Calculate the area of the first right triangular sail
    tri_sail1_base = 3
    tri_sail1_ht = 4
    tri_sail1_area = (tri_sail1_base * tri_sail1_ht) / 2

    # Calculate the area of the second right triangular sail
    tri_sail2_base = 4
    tri_sail2_ht = 6
    tri_sail2_area = (tri_sail2_base * tri_sail2_ht) / 2

    # Calculate the total area of canvas needed
    total_area = rect_sail_area + tri_sail1_area + tri_sail2_area
    result = total_area
    return result

print(solution())