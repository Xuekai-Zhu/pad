def solution():
    """Carrie works for $8 an hour and 35 hours a week at her job. It’s been a month since she started working there. She has saved up all of her money because she wants to buy a bike for $400. How much money will she have left over after she buys her bike?"""
    # Calculate Carrie's total earnings for the month
    hourly_rate = 8
    weekly_hours = 35
    total_hours = weekly_hours * 4 # assuming 4 weeks in a month
    total_earnings = hourly_rate * total_hours

    # Calculate Carrie's money left after buying the bike
    bike_price = 400
    money_left = total_earnings - bike_price

    # Display the result
    result = money_left
    return result

print(solution())