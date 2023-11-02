def solution():
    """Carrie works for $8 an hour and 35 hours a week at her job. It’s been a month since she started working there. She has saved up all of her money because she wants to buy a bike for $400. How much money will she have left over after she buys her bike?"""
    hourly_rate = 8
    hours_per_week = 35
    weeks_per_month = 4
    total_earned = hourly_rate * hours_per_week * weeks_per_month
    bike_cost = 400
    money_left = total_earned - bike_cost
    result = money_left
    return result

print(solution())