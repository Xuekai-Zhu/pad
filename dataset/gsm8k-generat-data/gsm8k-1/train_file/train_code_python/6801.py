def solution():
    """Big boxes contain 7 dolls each. Small boxes contain 4 dolls each. There are 5 big boxes and 9 small boxes. How many dolls are there in total?"""
    big_box_dolls = 7
    small_box_dolls = 4
    num_big_boxes = 5
    num_small_boxes = 9
    total_dolls = (big_box_dolls * num_big_boxes) + (small_box_dolls * num_small_boxes)
    result = total_dolls
    return result

print(solution())