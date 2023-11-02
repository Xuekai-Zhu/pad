def solution():
    msrp = 30  # The toaster costs $30 at MSRP
    insurance_plan = 0.20 * msrp  # The insurance plan costs 20% of the MSRP
    taxable_amount = msrp + insurance_plan  # The taxable amount includes the MSRP and the insurance plan
    state_tax = 0.50 * taxable_amount  # The state tax rate is 50% of the taxable amount

    # Calculate the total amount Jon must pay
    total_cost = msrp + insurance_plan + state_tax
    result = total_cost
    return result

print(solution())