def solution():
    """Buying a toaster requires an insurance plan that is 20% of the MSRP, plus a mandatory state tax rate of 50% after the insurance plan calculation.
    Jon chooses to buy a toaster that costs $30 at MSRP. What is the total he must pay?"""
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