def solution():
    """Marvin and Tina were selling candy bars to help fund their class trip. The candy bars cost $2 each. Marvin sold 35 candy bars total. Tina sold three times the number of candy bars as Marvin. How much more money did Tina make for the class trip selling candy bars compared to Marvin?"""
    marvin_candy_bars = 35
    tina_candy_bars = marvin_candy_bars * 3
    candy_bar_cost = 2
    marvin_money = marvin_candy_bars * candy_bar_cost
    tina_money = tina_candy_bars * candy_bar_cost
    tina_profit = tina_money - marvin_money
    result = tina_profit
    return result

print(solution())