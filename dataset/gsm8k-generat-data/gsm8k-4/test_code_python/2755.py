def solution():
    """At A.T. Cross Luxury Pens, a pencil sells at twenty-five cents while a pen sells at fifteen cents. Bowen buys 40 pens and 2/5 times more pencils than pens from A.T. Cross Luxury Pens. Calculate the total amount of money Bowen spends."""
    # Define the prices
    pencil_price = 0.25
    pen_price = 0.15
    
    # Calculate the number of pencils Bowen buys
    pencil_ratio = 2/5
    pen_quantity = 40
    pencil_quantity = pen_quantity * (1 + pencil_ratio)
    
    # Calculate the total cost of the pens and pencils
    pen_cost = pen_price * pen_quantity
    pencil_cost = pencil_price * pencil_quantity
    total_cost = pen_cost + pencil_cost
    
    result = total_cost
    return result

print(solution())