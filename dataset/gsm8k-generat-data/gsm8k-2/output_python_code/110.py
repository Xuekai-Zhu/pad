def solution():
    """Marvin and Tina were selling candy bars to help fund their class trip. The candy bars cost $2 each. Marvin sold 35 candy bars total. Tina sold three times the number of candy bars as Marvin. How much more money did Tina make for the class trip selling candy bars compared to Marvin?"""
    marvin_bars = 35
    tina_bars = 3 * marvin_bars
    marvin_profit = marvin_bars * 2
    tina_profit = tina_bars * 2
    difference = tina_profit - marvin_profit
    result = difference
    return result

print(solution())