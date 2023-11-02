def solution():
    first_square_area = 8 * 5
    second_square_area = 10 * 7
    third_square_area = 5 * 5
    total_area = first_square_area + second_square_area + third_square_area
    flag_height = total_area / 15
    result = flag_height
    return result

print(solution())