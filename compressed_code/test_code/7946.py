def solution():
    
    total_laps = 98
    laps_on_saturday = 27
    laps_on_sunday_morning = 15
    laps_remaining = total_laps - laps_on_saturday - laps_on_sunday_morning
    result = laps_remaining
    return result

print(solution())