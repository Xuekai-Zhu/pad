def solution():
    # Calculate the total cost of the shoes before tax
    total_cost_before_tax = 150 + 120

    # Calculate the tax amount
    tax = 0.1 * total_cost_before_tax

    # Calculate the total amount paid including tax
    total_cost = total_cost_before_tax + tax
    result = total_cost
    return result

print(solution())