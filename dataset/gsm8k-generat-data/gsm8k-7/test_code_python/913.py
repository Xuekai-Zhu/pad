def solution():
    profit = 960
    goal = 610
    donations = 310

    # Calculate half of the profit
    half_profit = profit / 2

    # Calculate the total amount of money the trader has now
    total_money = half_profit + donations

    # Calculate how much money the trader made above her goal
    money_above_goal = total_money - goal
    result = money_above_goal
    return result

print(solution())