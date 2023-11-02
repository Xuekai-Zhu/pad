def solution():
    """Frankie and Carla played 30 games of ping pong against each other. Frankie won half as many games as did Carla. How many games did Carla win?"""
    total_games = 30
    carla_games = total_games * 2 / 3
    frankie_games = total_games - carla_games
    result = carla_games
    return result

print(solution())