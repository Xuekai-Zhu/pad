def solution():
    """Alton owns a business. He is currently renting a space that costs $20 per week. If Alton earns $8 per day, how much is his total profit every week?"""
    
    # Define the cost of rent per week and the amount Alton earns per day
    RENT_COST = 20
    DAILY_EARNINGS = 8

    # Calculate Alton's total earnings for the week
    weekly_earnings = DAILY_EARNINGS * 7

    # Calculate Alton's total profit for the week
    weekly_profit = weekly_earnings - RENT_COST

    # Display Alton's total profit for the week
    result = weekly_profit
    return result

print(solution())