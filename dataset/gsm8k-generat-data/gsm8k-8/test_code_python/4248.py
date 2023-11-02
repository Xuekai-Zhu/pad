def solution():
    total_distance = 99
    lap_distance = 9
    completed_laps = 6

    remaining_distance = total_distance - (completed_laps * lap_distance)
    full_laps = remaining_distance // lap_distance
    result = full_laps
    return result

print(solution())