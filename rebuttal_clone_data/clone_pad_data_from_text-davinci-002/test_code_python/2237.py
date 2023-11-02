def solution():
    birthday_money = 100
    video_game_cost = birthday_money / 4
    goggles_cost = (birthday_money - video_game_cost) / 5
    money_left = birthday_money - video_game_cost - goggles_cost
    result = money_left
    return result

print(solution())