def solution():
    
    loaves_per_hour = 5
    ovens = 4
    weekday_hours = 5
    weekend_hours = 2
    weekday_loaves = loaves_per_hour * ovens * weekday_hours
    weekend_loaves = loaves_per_hour * ovens * weekend_hours
    weekly_loaves = weekday_loaves * 5 + weekend_loaves * 2
    total_loaves = weekly_loaves * 3
    result = total_loaves
    return result

print(solution())