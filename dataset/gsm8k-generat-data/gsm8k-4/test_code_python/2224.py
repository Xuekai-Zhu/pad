def solution():
    """Samuel is arranging his grandma’s teacups. They are stored in boxes and inside the boxes, they are stacked 5 rows high with 4 cups in each row.
    Of the 26 boxes in her attic, 6 of the boxes contain pans, half of the remaining boxes contain decorations, and the rest of the boxes contain her teacups.
    Samuel breaks 2 of the cups every time he picks up one of the boxes. By the time Samuel has taken all of the teacups out of the boxes, how many teacups are left?"""
    # Define the number of boxes and the number of cups in each box
    boxes = 26
    rows = 5
    cups_per_row = 4

    # Calculate the total number of teacups
    total_cups = boxes * rows * cups_per_row

    # Calculate the number of boxes that contain pans
    pans_boxes = 6

    # Calculate the number of boxes that do not contain pans
    remaining_boxes = boxes - pans_boxes

    # Calculate the number of boxes that contain decorations
    decorations_boxes = remaining_boxes / 2

    # Calculate the number of boxes that contain teacups
    teacups_boxes = remaining_boxes - decorations_boxes

    # Calculate the number of cups broken by Samuel
    cups_broken = teacups_boxes * 2

    # Calculate the number of cups left
    cups_left = total_cups - cups_broken

    result = cups_left
    return result

print(solution())