def solution():
    """Kristy, a sales representative earns a basic salary of $7.50 per hour plus a 16% commission on everything she sells. This month, she worked for 160 hours and sold $25000 worth of items. Her monthly budget for food, clothing, rent, transportation, bills and savings is 95% of her total monthly earnings and the rest will be put towards insurance. How much did she allocate to insurance?"""
    # Define the hourly pay rate and commission percentage
    hourly_pay_rate = 7.5
    commission_percentage = 0.16

    # Define the number of hours worked and total sales made
    hours_worked = 160
    total_sales = 25000

    # Calculate the total earnings for the month
    earnings = (hourly_pay_rate * hours_worked) + (total_sales * commission_percentage)

    # Calculate the total budget for food, clothing, rent, transportation, bills and savings
    total_budget = earnings * 0.95

    # Calculate the amount allocated to insurance
    insurance_amount = earnings - total_budget

    result = insurance_amount
    return result

print(solution())