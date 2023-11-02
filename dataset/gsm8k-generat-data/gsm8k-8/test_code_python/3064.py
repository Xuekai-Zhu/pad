def solution():
    # Calculate the insurance plan cost
    insurance_cost = 0.2 * 30

    # Calculate the cost after insurance but before tax
    cost_after_insurance = 30 + insurance_cost

    # Calculate the tax amount
    tax_rate = 0.5
    tax_amount = tax_rate * cost_after_insurance

    # Calculate the total cost
    total_cost = cost_after_insurance + tax_amount
    result = total_cost
    return result

print(solution())