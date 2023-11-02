def solution():
    cost = 200  # Earbuds cost $200
    tax_rate = 0.15  # Tax rate is 15%

    # Calculate the tax amount
    tax = cost * tax_rate

    # Add the tax to the cost to get the total amount paid
    total_cost = cost + tax
    result = total_cost
    return result

print(solution())