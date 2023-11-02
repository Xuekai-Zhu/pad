def solution():
    # Calculate the total number of cans needed
    total_cans = 5 * 12 * 2

    # Calculate the total number of boxes needed
    total_boxes = total_cans / 10

    # Calculate the total cost of the boxes
    total_cost = total_boxes * 2

    # Calculate the cost per family member
    cost_per_member = total_cost / 6
    result = cost_per_member
    return result

print(solution())