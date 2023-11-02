def solution():
    
    msrp = 30
    insurance_plan = 0.2 * msrp
    taxable_amount = msrp + insurance_plan
    state_tax_rate = 0.5
    state_tax = state_tax_rate * taxable_amount
    total_cost = msrp + insurance_plan + state_tax
    result = total_cost
    return result

print(solution())