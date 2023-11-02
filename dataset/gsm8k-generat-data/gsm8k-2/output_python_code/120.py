def solution():
    """Carrie works for $8 an hour and 35 hours a week at her job. It’s been a month since she started working there. She has saved up all of her money because she wants to buy a bike for $400. How much money will she have left over after she buys her bike?"""
    hourly_rate = 8
    hours_per_week = 35
    weeks_in_month = 4
    total_earnings = hourly_rate * hours_per_week * weeks_in_month
    bike_cost = 400
    money_left_over = total_earnings - bike_cost
    result = money_left_over
    return result

print(solution())