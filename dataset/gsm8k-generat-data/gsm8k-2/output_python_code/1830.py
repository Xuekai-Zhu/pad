def solution():
    """A store ordered 300 more than twice as many pens as it did pencils at $5 each. If the cost of a pencil was $4, and the store ordered 15 boxes, each having 80 pencils, calculate the total amount of money they paid for the stationery."""
    pencil_price = 4
    pen_price = 5
    pencil_amount = 15 * 80
    pen_amount = 300 + 2 * pencil_amount
    total_amount = pencil_amount * pencil_price + pen_amount * pen_price
    result = total_amount
    return result

print(solution())