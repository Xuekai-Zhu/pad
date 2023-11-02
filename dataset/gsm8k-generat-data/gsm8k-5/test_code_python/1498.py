def solution():
    # Calculate Kristy's total earnings, including commission
    base_salary = 7.5 * 160  # Kristy earns a basic salary of $7.50 per hour, and she worked for 160 hours
    commission = 0.16 * 25000  # Kristy earns a 16% commission on everything she sells, and she sold $25000 worth of items
    total_earnings = base_salary + commission

    # Calculate Kristy's budget for food, clothing, rent, transportation, bills, and savings
    monthly_budget = 0.95 * total_earnings

    # Calculate the amount allocated to insurance
    insurance_amount = total_earnings - monthly_budget
    result = insurance_amount
    return result

print(solution())