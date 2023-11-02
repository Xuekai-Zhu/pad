def solution():
    # Calculate the total number of teacups in all boxes
    total_teacups = 26 * 5 * 4  # 26 boxes, 5 rows in each box, 4 cups in each row

    # Calculate the number of boxes that do not contain pans or decorations
    non_pan_boxes = 26 - 6  # 6 boxes contain pans
    non_pan_decoration_boxes = non_pan_boxes // 2  # Half of the remaining boxes contain decorations
    teacup_boxes = non_pan_boxes - non_pan_decoration_boxes  # The rest of the boxes contain teacups

    # Calculate the total number of teacups Samuel breaks
    total_broken_cups = 2 * teacup_boxes

    # Calculate the number of teacups left after Samuel breaks them
    teacups_left = total_teacups - total_broken_cups
    result = teacups_left
    return result

print(solution())