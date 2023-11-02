def solution():
    
    mondays_rain = 1.5
    tuesdays_rain = 2.5
    mondays_count = 7
    tuesdays_count = 9
    total_mondays_rain = mondays_rain * mondays_count
    total_tuesdays_rain = tuesdays_rain * tuesdays_count
    difference = total_tuesdays_rain - total_mondays_rain
    result = difference
    return result

print(solution())