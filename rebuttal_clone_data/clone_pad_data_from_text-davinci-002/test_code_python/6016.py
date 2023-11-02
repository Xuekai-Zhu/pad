def solution():
    total_meters = 2400
    meters_per_lap = 150
    laps_run = 6
    total_laps = total_meters / meters_per_lap
    laps_remaining = total_laps - laps_run
    result = laps_remaining
    
    return result

print(solution())