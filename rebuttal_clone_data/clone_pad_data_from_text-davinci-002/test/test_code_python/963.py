def solution():
    rain_on_mondays = 1.5
    rain_on_tuesdays = 2.5
    mondays_per_week = 7
    tuesdays_per_week = 9
    total_rain_on_mondays = rain_on_mondays * mondays_per_week
    total_rain_on_tuesdays = rain_on_tuesdays * tuesdays_per_week
    difference = total_rain_on_tuesdays - total_rain_on_mondays
    result = difference
    
    return result

print(solution())