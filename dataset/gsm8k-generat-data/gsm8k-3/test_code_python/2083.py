def solution():
    """James buys pistachios for $10 per can.  Each can is 5 ounces.  He eats 30 ounces of pistachios every 5 days.  How much does he spend on pistachios per week?"""
    # Define the cost per can and the number of ounces he eats every 5 days
    COST_PER_CAN = 10
    OUNCES_PER_5_DAYS = 30

    # Calculate the number of cans he needs to buy every 5 days
    cans_per_5_days = OUNCES_PER_5_DAYS / 5

    # Calculate the cost of the pistachios per 5 days
    cost_per_5_days = cans_per_5_days * COST_PER_CAN

    # Calculate the cost of the pistachios per week
    cost_per_week = cost_per_5_days * 7 / 5

    # Display the cost per week
    result = cost_per_week
    return result

print(solution())