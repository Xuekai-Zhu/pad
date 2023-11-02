def solution():
    sugar_per_bar = 1.5
    bars_per_minute = 36
    minutes = 2
    total_bars = bars_per_minute * minutes
    total_sugar = total_bars * sugar_per_bar
    result = total_sugar
    return result

print(solution())