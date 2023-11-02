def solution():
    """Kristy, a sales representative earns a basic salary of $7.50 per hour plus a 16% commission on everything she sells. This month, she worked for 160 hours and sold $25000 worth of items. Her monthly budget for food, clothing, rent, transportation, bills and savings is 95% of her total monthly earnings and the rest will be put towards insurance. How much did she allocate to insurance?"""
    # Define Kristy's hourly rate and commission percentage
    HOURLY_RATE = 7.50
    COMMISSION_PERCENTAGE = 0.16

    # Get the number of hours Kristy worked and the amount she sold
    hours_worked = 160
    sales = 25000

    # Calculate Kristy's earnings
    earnings = hours_worked * HOURLY_RATE + sales * COMMISSION_PERCENTAGE

    # Calculate Kristy's budget and insurance allocation
    budget = earnings * 0.95
    insurance = earnings - budget

    # Display Kristy's insurance allocation
    result = insurance
    return result

print(solution())