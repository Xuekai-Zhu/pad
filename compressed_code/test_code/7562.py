def solution():
    
    total_money = 100
    video_game_cost = total_money * 0.25
    money_left_after_video_game = total_money - video_game_cost
    goggles_cost = money_left_after_video_game * 0.2
    money_left = money_left_after_video_game - goggles_cost
    result = money_left
    return result

print(solution())