def solution():
    big_rectangle_length = 40
    big_rectangle_width = 20

    small_rectangle_length = big_rectangle_length / 2
    small_rectangle_width = big_rectangle_width / 2

    # Calculate the area of the smaller rectangle
    small_rectangle_area = small_rectangle_length * small_rectangle_width
    result = small_rectangle_area
    return result

print(solution())