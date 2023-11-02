def solution():
    allowance_week1to8 = 5
    allowance_week9to14 = 6
    savings = allowance_week1to8 * 8 + allowance_week9to14 * 6
    clothes_cost = savings / 2
    video_game_cost = 35
    remaining_money = savings - clothes_cost - video_game_cost
    result = remaining_money
    return result

print(solution())