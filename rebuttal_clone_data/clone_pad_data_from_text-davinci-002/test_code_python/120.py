def solution():
    """Carrie works for $8 an hour and 35 hours a week at her job. It’s been a month since she started working there. She has saved up all of her money because she wants to buy a bike for $400. How much money will she have left over after she buys her bike?"""
    hourly_wage = 8
    hours_worked = 35
    weeks_worked = 4
    total_hours = hours_worked * weeks_worked
    total_wage = hourly_wage * total_hours
    bike_cost = 400
    money_left = total_wage - bike_cost
    result = money_left
    return result

print(solution())