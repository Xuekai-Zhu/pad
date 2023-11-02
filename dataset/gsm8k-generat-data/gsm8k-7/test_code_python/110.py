def solution():
    candy_bar_cost = 2
    marvin_sales = 35
    tina_sales = 3 * marvin_sales
    marvin_profit = marvin_sales * candy_bar_cost
    tina_profit = tina_sales * candy_bar_cost
    extra_profit = tina_profit - marvin_profit
    result = extra_profit
    return result

print(solution())