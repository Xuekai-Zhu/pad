def solution():
    cost_of_mouse = 120
    cost_of_lefty_mouse = (cost_of_mouse * 30) / 100 + cost_of_mouse
    mice_sold = 25
    number_of_days = 7 - 3
    weekly_profit = number_of_days * mice_sold * cost_of_lefty_mouse
    result = weekly_profit
    return result

print(solution())