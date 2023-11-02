def solution():
    """Mike watches TV for 4 hours every day. On the days he plays video games he plays for half as long as he watches TV. If he plays video games 3 days a week how long does he spend watching TV and playing video games?"""
    tv_hours_per_day = 4
    video_game_hours_per_day = tv_hours_per_day / 2
    days_per_week = 7
    video_game_days_per_week = 3
    tv_hours_per_week = tv_hours_per_day * (days_per_week - video_game_days_per_week)
    video_game_hours_per_week = video_game_hours_per_day * video_game_days_per_week
    total_hours = tv_hours_per_week + video_game_hours_per_week
    result = total_hours
    return result

print(solution())