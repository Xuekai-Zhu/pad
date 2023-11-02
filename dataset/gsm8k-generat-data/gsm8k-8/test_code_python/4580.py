def solution():
    # Define the number of tied and lost games
    tied_games = 40
    lost_games = 30 / 2  # since losing a game costs $2

    # Calculate the total number of played games
    total_games = 100

    # Calculate the number of won games
    won_games = total_games - tied_games - lost_games

    result = won_games
    return result

print(solution())