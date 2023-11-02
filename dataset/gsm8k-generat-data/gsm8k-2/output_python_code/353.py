def solution():
    """Seth bought some boxes of oranges. He gave a box to his mother. He then gave away half of the remaining boxes. If Seth has 4 boxes of oranges left, how many boxes did he buy in the first place?"""
    remaining_boxes = 4
    after_mothers_day = remaining_boxes + 1
    before_half_given_away = after_mothers_day * 2
    total_boxes = before_half_given_away

    result = total_boxes
    return result

print(solution())