def solution():
    race_length = 12
    laps_run = 24
    lap_length = 100
    total_distance = laps_run * lap_length
    total_time = race_length * 60
    average_speed = total_distance / total_time
    average_earnings = (average_speed * 60) * 3.5
    result = average_earnings
    return result

print(solution())