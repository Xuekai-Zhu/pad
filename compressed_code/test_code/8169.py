def solution():
    
    ladies_walk_group = 3
    jamie_extra_miles_per_day = 2
    sue_extra_miles_per_day = jamie_extra_miles_per_day / 2
    days_per_week = 6
    total_ladies_walk_miles = (ladies_walk_group + jamie_extra_miles_per_day) * days_per_week + (sue_extra_miles_per_day * days_per_week)
    result = total_ladies_walk_miles
    return result

print(solution())