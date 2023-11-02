def solution():
    
    bars_per_day = 5000
    days_per_week = 7
    weeks = 2
    total_bars = bars_per_day * days_per_week * weeks
    price_per_bar = 2
    total_money = total_bars * price_per_bar
    result = total_money
    return result

print(solution())