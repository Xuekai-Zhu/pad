def solution():
    num_boxes = 4
    num_matchboxes_per_box = 20
    num_sticks_per_matchbox = 300

    # Calculate the total number of matchboxes Farrah ordered
    total_matchboxes = num_boxes * num_matchboxes_per_box

    # Calculate the total number of match sticks Farrah ordered
    total_sticks = total_matchboxes * num_sticks_per_matchbox
    result = total_sticks
    return result

print(solution())