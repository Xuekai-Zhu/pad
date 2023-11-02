def solution():
    
    profit = 960
    goal = 610
    donations = 310
    half_profit = profit / 2
    total_money = half_profit + donations
    money_above_goal = total_money - goal
    result = money_above_goal
    return result

print(solution())