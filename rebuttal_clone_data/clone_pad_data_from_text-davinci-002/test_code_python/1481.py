def solution():
     tv_hours_per_day = 4
     video_game_hours_per_day = tv_hours_per_day / 2
     days_per_week = 7
     days_playing_video_games = 3
     tv_hours_per_week = tv_hours_per_day * (days_per_week - days_playing_video_games)
     video_game_hours_per_week = video_game_hours_per_day * days_playing_video_games
     total_hours = tv_hours_per_week + video_game_hours_per_week
     result = total_hours
     return result

print(solution())