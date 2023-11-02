def solution():
    # Calculate Kristy's earnings from salary and commission
    salary = 7.5 * 160
    commission = 0.16 * 25000
    total_earnings = salary + commission

    # Calculate Kristy's budget for necessities
    necessary_expenses = 0.95 * total_earnings

    # Calculate Kristy's allocation for insurance
    insurance_allocation = total_earnings - necessary_expenses
    result = insurance_allocation
    return result

print(solution())