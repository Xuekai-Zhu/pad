def solution():
    
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