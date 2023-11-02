def solution():
    # Calculate the cost of one box
    box_cost = 80 + 165

    # Calculate the cost of 400 boxes
    initial_cost = box_cost * 400

    # Calculate the amount donated by the anonymous donor
    donation = 4 * initial_cost

    # Calculate the new total cost
    new_total_cost = initial_cost + donation

    # Calculate the number of boxes they can pack with the new total cost
    new_total_boxes = new_total_cost / box_cost

    result = new_total_boxes
    return result

print(solution())