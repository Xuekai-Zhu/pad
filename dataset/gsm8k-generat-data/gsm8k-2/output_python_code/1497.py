def solution():
    """
    Kristy, a sales representative earns a basic salary of $7.50 per hour plus a 16% commission on everything she sells.
    This month, she worked for 160 hours and sold $25000 worth of items.
    Her monthly budget for food, clothing, rent, transportation, bills and savings is 95% of her total monthly earnings and the rest will be put towards insurance.
    How much did she allocate to insurance?
    """
    hourly_rate = 7.5
    commission_rate = 0.16
    hours_worked = 160
    items_sold = 25000

    basic_salary = hourly_rate * hours_worked
    commission = commission_rate * items_sold
    total_earnings = basic_salary + commission

    monthly_budget = 0.95 * total_earnings
    insurance_allocation = total_earnings - monthly_budget

    return insurance_allocation

print(solution())