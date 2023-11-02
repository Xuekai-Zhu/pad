def solution():
    """Carrie works for $8 an hour and 35 hours a week at her job. It’s been a month since she started working there. She has saved up all of her money because she wants to buy a bike for $400. How much money will she have left over after she buys her bike?"""
    # Define Carrie's hourly wage and number of hours worked per week
    hourly_wage = 8
    weekly_hours = 35

    # Calculate Carrie's total earnings for the month
    monthly_earnings = hourly_wage * weekly_hours * 4

    # Define the cost of the bike
    bike_cost = 400

    # Calculate the money left over after buying the bike
    money_left_over = monthly_earnings - bike_cost

    # return the result
    result = money_left_over
    return result

print(solution())