def solution():
    onur_daily_distance = 250
    hanil_daily_distance = onur_daily_distance + 40
    weekly_distance = 5 * (onur_daily_distance + hanil_daily_distance)
    result = weekly_distance
    return result

print(solution())