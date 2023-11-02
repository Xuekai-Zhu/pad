def solution():
    
    
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