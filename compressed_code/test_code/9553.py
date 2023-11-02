def solution():
    
    vitamin_per_pill = 50
    recommended_daily_vitamin = 200
    pills_per_day = recommended_daily_vitamin / vitamin_per_pill
    pills_per_week = pills_per_day * 7
    result = pills_per_week
    return result

print(solution())