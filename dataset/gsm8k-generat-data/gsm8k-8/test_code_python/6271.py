def solution():
    # Calculate the amount of sales tax
    sales_tax = 0.04 * 100

    # Calculate the amount of the tip
    tip = 0.06 * 100

    # Calculate the total cost of the lunch
    total_cost = 100 + sales_tax + tip

    result = total_cost
    return result

print(solution())