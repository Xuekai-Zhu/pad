def solution():
    vitamin_per_pill = 50 # mg
    daily_target = 200 # mg
    pills_per_day = daily_target / vitamin_per_pill # pills
    pills_per_week = pills_per_day * 7 # pills
    result = pills_per_week
    return result

print(solution())