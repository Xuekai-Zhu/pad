def solution():
    """Harold's fancy wrapping paper can wrap 5 shirt boxes or 3 XL boxes. For the upcoming holiday, he has 20 shirt boxes to wrap and 12 XL boxes to wrap. If each roll of wrapping paper costs $4.00 per roll, how much will he spend to wrap all of the boxes?"""
    shirt_boxes_per_roll = 5
    xl_boxes_per_roll = 3
    shirt_boxes_to_wrap = 20
    xl_boxes_to_wrap = 12
    total_shirt_rolls_needed = shirt_boxes_to_wrap / shirt_boxes_per_roll
    total_xl_rolls_needed = xl_boxes_to_wrap / xl_boxes_per_roll
    total_rolls_needed = total_shirt_rolls_needed + total_xl_rolls_needed
    cost_per_roll = 4.00
    cost_to_wrap_all_boxes = total_rolls_needed * cost_per_roll
    result = cost_to_wrap_all_boxes
    return result

print(solution())