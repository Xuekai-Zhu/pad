def solution():
    """Zach is saving his money to buy a brand new bike that costs $100. His weekly allowance is $5. His parent will pay him an extra $10 to mow the lawn. His neighbor will pay him $7 per hour to babysit their son. He has already saved up $65. He'll receive his allowance on Friday and he's planning on babysitting for 2 hours this Saturday after he mows the lawn. How much more money does Zach need to earn before he can buy the bike?"""
    bike_cost = 100
    current_savings = 65
    weekly_allowance = 5
    lawn_payment = 10
    babysitting_hours = 2
    babysitting_rate = 7

    total_weekly_income = weekly_allowance + lawn_payment + (babysitting_hours * babysitting_rate)
    money_needed = bike_cost - current_savings - total_weekly_income
    result = money_needed
    return result

print(solution())