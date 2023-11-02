def solution():
    total_games = 30

    # Let x be the number of games Carla won
    # Then Frankie won half as many, or x/2
    x = total_games * 2 / 3  # Carla won 2/3 of the total games

    # Calculate the number of games Frankie won
    y = total_games - x

    result = x  # Carla won x games
    return result

print(solution())