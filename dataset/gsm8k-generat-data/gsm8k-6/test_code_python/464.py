def solution():
    # Calculate the number of games Frankie and Carla won
    total_games = 30
    carla_games = total_games * 2 / 3  # Carla won 2/3 of the total games
    frankie_games = total_games - carla_games  # Frankie won the rest of the games

    result = carla_games
    return result

print(solution())