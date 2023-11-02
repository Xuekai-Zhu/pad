def solution():
    total_games = 30
    carla_win = (total_games / 3) * 2
    frankie_win = total_games - carla_win
    result = carla_win
    return result

print(solution())