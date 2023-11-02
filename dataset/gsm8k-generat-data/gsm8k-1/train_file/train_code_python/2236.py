def solution():
    """On Mary's birthday, her brother surprised her with $100. She spent a quarter of it on a new video game and then used a fifth of what was left on swimming goggles. How much money did she have left?"""
    total_money = 100
    video_game_cost = total_money * 0.25
    money_left_after_video_game = total_money - video_game_cost
    goggles_cost = money_left_after_video_game * 0.2
    money_left = money_left_after_video_game - goggles_cost
    result = money_left
    return result

print(solution())