def solution():
    
    walking_calories_per_hour = 300
    dancing_calories_per_hour = walking_calories_per_hour * 2
    daily_dancing_calories_lost = dancing_calories_per_hour * 0.5 * 2
    total_dancing_calories_lost_per_week = daily_dancing_calories_lost * 4
    result = total_dancing_calories_lost_per_week
    return result

print(solution())