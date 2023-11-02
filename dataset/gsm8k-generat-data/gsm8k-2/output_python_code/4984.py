def solution():
    """A rectangle has a length of 40 meters and a width of 20 meters. A similar smaller rectangle has half the length and width of the big rectangle. What's the area of the smaller rectangle?"""
    big_rectangle_length = 40
    big_rectangle_width = 20
    small_rectangle_length = big_rectangle_length / 2
    small_rectangle_width = big_rectangle_width / 2
    small_rectangle_area = small_rectangle_length * small_rectangle_width
    result = small_rectangle_area
    return result

print(solution())