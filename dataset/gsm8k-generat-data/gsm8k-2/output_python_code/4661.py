def solution():
    """Zach is saving his money to buy a brand new bike that costs $100. His weekly allowance is $5. His parent will pay him an extra $10 to mow the lawn. His neighbor will pay him $7 per hour to babysit their son. He has already saved up $65. He'll receive his allowance on Friday and he's planning on babysitting for 2 hours this Saturday after he mows the lawn. How much more money does Zach need to earn before he can buy the bike?"""
    bike_cost = 100
    saved_money = 65
    weekly_allowance = 5
    lawn_mowing_payment = 10
    babysitting_payment = 7 * 2
    total_money_earned = saved_money + weekly_allowance + lawn_mowing_payment + babysitting_payment
    money_left_to_save = bike_cost - total_money_earned
    result = money_left_to_save
    return result

print(solution())