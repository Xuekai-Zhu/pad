def solution():
    tv_hours_per_day = 4
    video_games_hours_per_day = tv_hours_per_day / 2
    num_video_game_days_per_week = 3

    # Calculate the total hours spent watching TV per week
    tv_hours_per_week = tv_hours_per_day * 7

    # Calculate the total hours spent playing video games per week
    video_game_hours_per_week = video_games_hours_per_day * num_video_game_days_per_week

    # Calculate the total hours spent watching TV and playing video games per week
    total_hours_per_week = tv_hours_per_week + video_game_hours_per_week
    result = total_hours_per_week
    return result

print(solution())