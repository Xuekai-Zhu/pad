def solution():
    """Alton owns a business. He is currently renting a space that costs $20 per week. If Alton earns $8 per day, how much is his total profit every week?"""
    # Define the cost of rent and the daily earnings
    rent_cost = 20
    daily_earnings = 8

    # Calculate the total earnings for a week
    weekly_earnings = daily_earnings * 7

    # Calculate the profit for a week
    weekly_profit = weekly_earnings - rent_cost

    # Return the result
    result = weekly_profit
    return result

print(solution())