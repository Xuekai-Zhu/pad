def solution():
    point_guard = 130
    shooting_guard = 145
    small_forward = 85
    power_forward = 60
    center = 180
    total_seconds = point_guard + shooting_guard + small_forward + power_forward + center
    total_players = 5
    average_seconds = total_seconds / total_players
    minutes = average_seconds / 60
    result = minutes
    return result

print(solution())