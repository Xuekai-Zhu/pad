def solution():
    """Toby has two rectangles of cloth. The first is 4 inches wide and 5 inches tall. The second is 3 inches wide and 6 inches tall. How many more square inches is the area of the first compared to the second?"""
    rectangle_1_width = 4
    rectangle_1_height = 5
    rectangle_2_width = 3
    rectangle_2_height = 6
    rectangle_1_area = rectangle_1_width * rectangle_1_height
    rectangle_2_area = rectangle_2_width * rectangle_2_height
    area_difference = rectangle_1_area - rectangle_2_area
    result = area_difference
    return result

print(solution())