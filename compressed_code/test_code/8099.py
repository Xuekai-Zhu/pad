def solution():
    
    total_bars = 20
    bars_per_day = 7
    bars_set_aside = bars_per_day
    bars_traded = 3
    bars_given_away = total_bars - bars_set_aside - bars_traded
    num_sisters = 2
    bars_per_sister = bars_given_away / num_sisters
    result = bars_per_sister
    return result

print(solution())