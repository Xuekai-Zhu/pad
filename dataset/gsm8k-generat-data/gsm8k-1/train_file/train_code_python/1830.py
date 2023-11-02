def solution():
    """A store ordered 300 more than twice as many pens as it did pencils at $5 each. If the cost of a pencil was $4, and the store ordered 15 boxes, each having 80 pencils, calculate the total amount of money they paid for the stationery."""
    # calculate the total number of pencils ordered
    pencils_per_box = 80
    num_boxes = 15
    total_pencils_ordered = pencils_per_box * num_boxes

    # calculate the total number of pens ordered
    pens_ordered = (2 * total_pencils_ordered) + 300

    # calculate the total cost of the pens and pencils
    cost_of_pencils = total_pencils_ordered * 4
    cost_of_pens = pens_ordered * 5
    total_cost = cost_of_pencils + cost_of_pens

    result = total_cost
    return result

print(solution())