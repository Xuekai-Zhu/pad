def solution():
    """Samuel is arranging his grandma’s teacups. They are stored in boxes and inside the boxes, they are stacked 5 rows high with 4 cups in each row. Of the 26 boxes in her attic, 6 of the boxes contain pans, half of the remaining boxes contain decorations, and the rest of the boxes contain her teacups. Samuel breaks 2 of the cups every time he picks up one of the boxes. By the time Samuel has taken all of the teacups out of the boxes, how many teacups are left?"""
    total_boxes = 26
    pans_boxes = 6
    decorations_boxes = (total_boxes - pans_boxes) // 2
    teacups_boxes = total_boxes - pans_boxes - decorations_boxes
    cups_per_box = 5 * 4
    total_cups = teacups_boxes * cups_per_box
    cups_breaking = teacups_boxes * 2
    cups_left = total_cups - cups_breaking
    result = cups_left
    return result

print(solution())