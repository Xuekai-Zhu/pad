def solution():
    # Calculate the cost of the milk and bananas before tax
    milk_cost = 3
    banana_cost = 2
    total_cost_before_tax = milk_cost + banana_cost

    # Calculate the amount of tax
    tax_rate = 0.2
    tax_amount = total_cost_before_tax * tax_rate

    # Calculate the total cost with tax
    total_cost_with_tax = total_cost_before_tax + tax_amount

    result = total_cost_with_tax
    return result

print(solution())