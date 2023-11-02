def solution():
    """Frankie and Carla played 30 games of ping pong against each other. Frankie won half as many games as did Carla. How many games did Carla win?"""
    # Define the total number of games played
    total_games = 30

    # Calculate the number of games won by Frankie and Carla
    carla_wins = 2 * (total_games / 3)
    frankie_wins = total_games - carla_wins

    # Return the number of games won by Carla
    result = carla_wins
    return result

print(solution())