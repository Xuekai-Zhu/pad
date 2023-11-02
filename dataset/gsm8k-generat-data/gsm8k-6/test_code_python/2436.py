def solution():
    # Calculate the number of boxes needed to ship the brochures
    brochures_per_box = 5000 / 5  # each box can only contain one-fifth of the brochures
    num_boxes = 5000 // brochures_per_box  # use integer division to get the whole number of boxes needed
    if 5000 % brochures_per_box != 0:  # if there are any remaining brochures that don't fit into whole boxes
        num_boxes += 1  # add an extra box to account for these remaining brochures
    result = num_boxes
    return result

print(solution())