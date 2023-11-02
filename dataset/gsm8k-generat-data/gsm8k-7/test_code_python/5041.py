def solution():
    total_area = 200

    # Calculate the area of the first three paintings
    painting1_area = 5 * 5
    painting2_area = 5 * 5
    painting3_area = 5 * 5

    # Calculate the area of the fourth painting
    painting4_area = 10 * 8

    # Calculate the total area of the first four paintings
    total_area_first4 = painting1_area + painting2_area + painting3_area + painting4_area

    # Calculate the area of the fifth painting
    painting5_height = 5
    painting5_width = (total_area - total_area_first4) / painting5_height
    result = painting5_width
    return result

print(solution())