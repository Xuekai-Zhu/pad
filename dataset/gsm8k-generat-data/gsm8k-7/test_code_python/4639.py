def solution():
    shots_per_period = (2*2 + 1*3) * 3  # 3 sets of 2+2+3 shots for each period
    total_shots = shots_per_period * 2  # 2 periods
    points_per_shot = 2  # 2 points per shot
    total_points = total_shots * points_per_shot
    result = total_points
    return result

print(solution())