def solution():
    initial_hours_read = 12
    initial_video_game_time = initial_hours_read * 30
    percent_increase = 20
    increase_amount = initial_video_game_time * (percent_increase / 100)
    video_game_time_with_raise = initial_video_game_time + increase_amount
    result = video_game_time_with_raise - initial_video_game_time
    
    return result

print(solution())