def solution():
    total_meters = 99
    meters_per_lap = 9
    laps_completed = 6
    total_laps = total_meters / meters_per_lap
    remaining_laps = total_laps - laps_completed
    result = remaining_laps
    return result

print(solution())