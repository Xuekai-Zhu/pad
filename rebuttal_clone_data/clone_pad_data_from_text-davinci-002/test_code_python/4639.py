def solution():
    shots_per_minute = 2
    points_per_shot_1 = 2
    points_per_shot_2 = 3
    minutes_per_period = 12
    periods = 2
    total_shots = shots_per_minute * minutes_per_period * periods
    total_points = total_shots * (points_per_shot_1 + points_per_shot_2) / 2
    result = total_points
    return result

print(solution())