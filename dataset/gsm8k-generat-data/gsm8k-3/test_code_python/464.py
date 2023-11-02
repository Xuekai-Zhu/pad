def solution():
    """Frankie and Carla played 30 games of ping pong against each other.  Frankie won half as many games as did Carla.  How many games did Carla win?"""
    # Let x be the number of games Carla won
    x = 2 * y # Frankie won half as many games as Carla
    total_games = 30 # They played 30 games in total
    y + x = total_games # Carla and Frankie won a total of 30 games
    y + 2y = 30 # Substitute x with 2y
    3y = 30 # Combine like terms
    y = 10 # Solve for y
    # Carla won 10 games
    result = y
    return result

print(solution())