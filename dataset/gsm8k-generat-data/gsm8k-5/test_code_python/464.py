def solution():
    total_games = 30  # Frankie and Carla played 30 games in total
    frankie_wins = total_games / 3  # Frankie won half as many games as Carla
    carla_wins = total_games - frankie_wins  # Carla won the remaining games

    result = carla_wins
    return result

print(solution())