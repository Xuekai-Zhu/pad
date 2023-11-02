def solution():
    # Define the number of boxes and matchboxes
    num_boxes = 4
    matchboxes_per_box = 20
    sticks_per_matchbox = 300

    # Calculate the total number of match sticks
    total_sticks = num_boxes * matchboxes_per_box * sticks_per_matchbox
    result = total_sticks
    return result

print(solution())