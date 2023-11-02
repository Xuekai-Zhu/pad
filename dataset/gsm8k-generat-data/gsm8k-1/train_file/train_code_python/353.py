def solution():
    """Seth bought some boxes of oranges. He gave a box to his mother. He then gave away half of the remaining boxes. If Seth has 4 boxes of oranges left, how many boxes did he buy in the first place?"""
    boxes_left = 4
    boxes_given_away = boxes_left * 2
    boxes_after_mother = boxes_given_away + 1
    total_boxes = boxes_after_mother
    result = total_boxes
    return result

print(solution())