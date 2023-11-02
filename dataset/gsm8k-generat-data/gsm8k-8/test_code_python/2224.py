def solution():
    # Calculate the total teacups before Samuel starts breaking them
    total_teacups = 26 * 5 * 4

    # Calculate the number of boxes that don't contain pans
    non_pans_boxes = 26 - 6

    # Calculate the number of boxes that contain decorations
    decoration_boxes = non_pans_boxes / 2

    # Calculate the number of teacup boxes
    teacup_boxes = non_pans_boxes - decoration_boxes

    # Calculate the total number of teacups in the teacup boxes
    teacup_total = teacup_boxes * 5 * 4

    # Calculate the number of teacups Samuel breaks
    teacups_broken = 2 * teacup_boxes * 5 * 4

    # Calculate the final number of teacups
    final_teacups = total_teacups - teacups_broken + teacup_total
    result = final_teacups
    return result

print(solution())