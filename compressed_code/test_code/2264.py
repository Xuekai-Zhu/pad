def solution():
    
    total_bars = 20
    bars_per_day = 7
    bars_left = total_bars - bars_per_day
    bars_traded = 3
    bars_given = bars_left - bars_traded
    bars_per_sister = bars_given / 2
    result = bars_per_sister
    return result

print(solution())