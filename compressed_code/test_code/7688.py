def solution():
    
    onur_daily_distance = 250
    hanil_daily_distance = onur_daily_distance + 40
    days_per_week = 5
    total_distance = (onur_daily_distance + hanil_daily_distance) * days_per_week
    result = total_distance
    return result

print(solution())