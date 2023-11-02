def solution():
    # Calculate the cost of T-shirts
    tshirt_cost = 8 * 6  # six T-shirts at $8 each

    # Calculate the cost of sweaters
    sweater_cost = 18 * 4  # four sweaters at $18 each

    # Calculate the cost of jackets
    jacket_cost = (80 * 5) * 0.9  # five jackets at $80 each with 10% discount

    # Calculate the subtotal
    subtotal = tshirt_cost + sweater_cost + jacket_cost

    # Calculate the sales tax
    sales_tax = subtotal * 0.05

    # Calculate the total cost
    total_cost = subtotal + sales_tax
    result = total_cost
    return result

print(solution())