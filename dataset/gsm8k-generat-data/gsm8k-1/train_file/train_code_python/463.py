def solution():
    """Frankie and Carla played 30 games of ping pong against each other. Frankie won half as many games as did Carla. How many games did Carla win?"""
    total_games = 30
    carla_win_percent = 0.67   #carla won 2/3rd of the total games, so her win percentage is 2/3=0.67
    carla_wins = round(total_games * carla_win_percent)
    result = carla_wins
    return result

print(solution())