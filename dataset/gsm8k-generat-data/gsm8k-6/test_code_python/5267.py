def solution():
    # Calculate the total cost of milk and bananas before tax
    cost_before_tax = 3 + 2  # $3 for a gallon of milk and $2 for a bunch of bananas

    # Calculate the amount of sales tax James paid
    sales_tax = 0.20 * cost_before_tax

    # Calculate the total cost, including sales tax
    total_cost = cost_before_tax + sales_tax
    result = total_cost
    return result

print(solution())