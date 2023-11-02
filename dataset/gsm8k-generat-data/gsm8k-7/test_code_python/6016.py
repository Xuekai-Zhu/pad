def solution():
    total_distance = 2400
    distance_per_lap = 150
    laps_per_person = 6
    total_laps = total_distance / distance_per_lap
    laps_completed = 2 * laps_per_person
    laps_remaining = total_laps - laps_completed
    result = laps_remaining
    return result

print(solution())