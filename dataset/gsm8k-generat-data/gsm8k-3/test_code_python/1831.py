def solution():
    """A store ordered 300 more than twice as many pens as it did pencils at $5 each. If the cost of a pencil was $4, and the store ordered 15 boxes, each having 80 pencils, calculate the total amount of money they paid for the stationery."""
    # Define the cost of pens and pencils
    PEN_COST = 5
    PENCIL_COST = 4

    # Calculate the number of pencils ordered
    pencils_ordered = 15 * 80

    # Calculate the number of pens ordered
    pens_ordered = 2 * pencils_ordered + 300

    # Calculate the cost of the pencils
    pencil_cost = pencils_ordered * PENCIL_COST

    # Calculate the cost of the pens
    pen_cost = pens_ordered * PEN_COST

    # Calculate the total cost
    total_cost = pencil_cost + pen_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())