def solution():
    # Calculate the total cost for the T-shirts
    tshirt_cost = 8 * 6

    # Calculate the total cost for the sweaters
    sweater_cost = 18 * 4

    # Calculate the total cost for the jackets after discount
    jacket_cost = (80 * 5) * 0.9

    # Calculate the subtotal before tax
    subtotal = tshirt_cost + sweater_cost + jacket_cost

    # Calculate the sales tax
    sales_tax = subtotal * 0.05

    # Calculate the total cost including tax
    total_cost = subtotal + sales_tax
    result = total_cost
    return result

print(solution())