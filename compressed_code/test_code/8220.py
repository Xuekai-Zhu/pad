def solution():
    
    msrp = 30
    insurance_rate = 0.2
    state_tax_rate = 0.5
    insurance_cost = msrp * insurance_rate
    taxable_amount = msrp + insurance_cost
    state_tax = taxable_amount * state_tax_rate
    total_cost = msrp + insurance_cost + state_tax
    result = total_cost
    return result

print(solution())