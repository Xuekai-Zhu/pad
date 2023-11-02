def solution():
    """A trader made a profit of $960 after a week of sales. To raise $610 to pay for her next shipment of wares, she splits the profit in half and solicits donations from her family and friends. If she received a total donation of $310 and adds it to one-half of her profit, how much money did she make above her goal?"""
    profit = 960
    goal = 610
    donations = 310
    half_profit = profit / 2
    total_money = half_profit + donations
    money_above_goal = total_money - goal
    result = money_above_goal
    return result

print(solution())