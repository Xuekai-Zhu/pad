def solution():
    
    video_game_cost = 60
    candy_cost = 5
    hours_worked = 9
    hourly_rate = 8
    money_earned = hourly_rate * hours_worked
    total_cost = video_game_cost + candy_cost
    money_left_over = money_earned - total_cost
    result = money_left_over
    return result

print(solution())