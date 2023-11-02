def solution():
    """Harold's fancy wrapping paper can wrap 5 shirt boxes or 3 XL boxes. For the upcoming holiday, he has 20 shirt boxes to wrap and 12 XL boxes to wrap. If each roll of wrapping paper costs $4.00 per roll, how much will he spend to wrap all of the boxes?"""
    shirt_boxes_per_roll = 5
    xl_boxes_per_roll = 3
    rolls_needed_for_shirt_boxes = 20 / shirt_boxes_per_roll
    rolls_needed_for_xl_boxes = 12 / xl_boxes_per_roll
    total_rolls_needed = rolls_needed_for_shirt_boxes + rolls_needed_for_xl_boxes
    cost_per_roll = 4.00
    total_cost = total_rolls_needed * cost_per_roll
    result = total_cost
    return result

print(solution())