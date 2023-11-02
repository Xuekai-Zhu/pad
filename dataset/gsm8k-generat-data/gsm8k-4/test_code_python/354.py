def solution():
    """Seth bought some boxes of oranges. He gave a box to his mother. He then gave away half of the remaining boxes. If Seth has 4 boxes of oranges left, how many boxes did he buy in the first place?"""
    # Define the number of boxes Seth has left
    boxes_left = 4

    # Calculate the number of boxes Seth had after giving one to his mother
    boxes_after_mother = boxes_left + 1

    # Calculate the number of boxes Seth had before giving away half
    boxes_before_half = boxes_after_mother * 2

    # Calculate the total number of boxes Seth bought
    total_boxes = boxes_before_half + 1

    # return the result
    result = total_boxes
    return result

print(solution())