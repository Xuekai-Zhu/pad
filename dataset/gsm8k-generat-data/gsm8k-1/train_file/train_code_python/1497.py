def solution():
    """Kristy, a sales representative earns a basic salary of $7.50 per hour plus a 16% commission on everything she sells. This month, she worked for 160 hours and sold $25000 worth of items. Her monthly budget for food, clothing, rent, transportation, bills and savings is 95% of her total monthly earnings and the rest will be put towards insurance. How much did she allocate to insurance?"""
    base_salary = 7.5
    commission_rate = 0.16
    hours_worked = 160
    items_sold = 25000
    total_earnings = (base_salary * hours_worked) + (commission_rate * items_sold)
    insurance_allocation = (1 - 0.95) * total_earnings
    result = insurance_allocation
    return result

print(solution())