def solution():
    """Samuel is arranging his grandma’s teacups. They are stored in boxes and inside the boxes, they are stacked 5 rows high with 4 cups in each row. Of the 26 boxes in her attic, 6 of the boxes contain pans, half of the remaining boxes contain decorations, and the rest of the boxes contain her teacups. Samuel breaks 2 of the cups every time he picks up one of the boxes. By the time Samuel has taken all of the teacups out of the boxes, how many teacups are left?"""
    
    boxes_total = 26
    pans_boxes = 6
    decoration_boxes = (boxes_total - pans_boxes) / 2
    teacups_boxes = boxes_total - pans_boxes - decoration_boxes
    cups_per_box = 5 * 4
    teacups_total = cups_per_box * teacups_boxes
    broken_cups_per_box = 2
    broken_cups_total = broken_cups_per_box * teacups_boxes
    teacups_left = teacups_total - broken_cups_total
    result = teacups_left
    
    return result

print(solution())