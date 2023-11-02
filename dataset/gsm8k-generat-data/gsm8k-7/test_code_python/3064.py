def solution():
    msrp = 30
    insurance_percent = 0.2
    state_tax_percent = 0.5

    # Calculate the cost of the insurance plan
    insurance_cost = msrp * insurance_percent

    # Calculate the subtotal after adding the insurance cost
    subtotal = msrp + insurance_cost

    # Calculate the cost of the state tax
    state_tax_cost = subtotal * state_tax_percent

    # Calculate the total cost
    total_cost = subtotal + state_tax_cost
    result = total_cost
    return result

print(solution())