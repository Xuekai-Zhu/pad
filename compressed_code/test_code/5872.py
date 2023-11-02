def solution():
    
    marvin_candy_bars = 35
    tina_candy_bars = marvin_candy_bars * 3
    candy_bar_cost = 2
    marvin_money = marvin_candy_bars * candy_bar_cost
    tina_money = tina_candy_bars * candy_bar_cost
    tina_profit = tina_money - marvin_money
    result = tina_profit
    return result

print(solution())