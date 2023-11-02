def solution():
    """A store ordered 300 more than twice as many pens as it did pencils at $5 each. If the cost of a pencil was $4, and the store ordered 15 boxes, each having 80 pencils, calculate the total amount of money they paid for the stationery."""
    # Calculate the total number of pencils ordered
    total_pencils = 15 * 80

    # Calculate the total number of pens ordered using the given relationship
    total_pens = 2 * total_pencils + 300

    # Calculate the total cost of the pencils
    pencil_cost = total_pencils * 4

    # Calculate the total cost of the pens
    pen_cost = total_pens * 5

    # Calculate the total cost of the stationery
    total_cost = pencil_cost + pen_cost

    result = total_cost
    return result

print(solution())