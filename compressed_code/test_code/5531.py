def solution():
    
    weekday_price = 0.5 * 3
    sunday_price = 2
    total_price_per_week = weekday_price + sunday_price
    total_price_over_8_weeks = total_price_per_week * 8
    result = total_price_over_8_weeks
    return result

print(solution())