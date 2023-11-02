def solution():
    """Buying a toaster requires an insurance plan that is 20% of the MSRP, plus a mandatory state tax rate of 50% after the insurance plan calculation. Jon chooses to buy a toaster that costs $30 at MSRP. What is the total he must pay?"""
    msrp = 30
    insurance_plan = 0.2 * msrp
    taxable_amount = msrp + insurance_plan
    state_tax_rate = 0.5
    state_tax = state_tax_rate * taxable_amount
    total_cost = msrp + insurance_plan + state_tax
    result = total_cost
    return result

print(solution())