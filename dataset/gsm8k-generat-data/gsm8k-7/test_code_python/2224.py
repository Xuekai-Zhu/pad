def solution():
    num_boxes = 26
    rows_per_box = 5
    cups_per_row = 4
    num_cups_per_box = rows_per_box * cups_per_row
    num_pans_boxes = 6

    # Calculate the number of boxes that do not contain pans
    num_non_pans_boxes = num_boxes - num_pans_boxes

    # Calculate the number of boxes that contain decorations
    num_decor_boxes = num_non_pans_boxes // 2

    # Calculate the number of boxes that contain teacups
    num_teacup_boxes = num_non_pans_boxes - num_decor_boxes

    # Calculate the total number of teacups
    total_teacups = num_teacup_boxes * num_cups_per_box

    # Calculate the number of teacups that Samuel breaks
    num_broken_cups = num_boxes * 2

    # Calculate the number of teacups left after Samuel takes them out of the boxes
    cups_left = total_teacups - num_broken_cups
    result = cups_left
    return result

print(solution())