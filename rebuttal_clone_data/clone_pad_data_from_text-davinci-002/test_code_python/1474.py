def solution():
    hours_watched_last_week = 10
    hours_watched_week_before = 8
    hours_watched_next_week = 12
    total_hours_watched = hours_watched_last_week + hours_watched_week_before + hours_watched_next_week
    average_hours_watched = total_hours_watched / 3
    result = average_hours_watched
    return result

print(solution())