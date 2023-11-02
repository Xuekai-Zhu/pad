def solution():
    
    total_bars = 100
    lost_bars = 20
    remaining_bars = total_bars - lost_bars
    friends = 4
    bars_each = remaining_bars // friends
    result = bars_each
    return result

print(solution())