def solution():
    """John hits 70% of his free throws. For every foul he gets 2 shots. He gets fouled 5 times a game. How many free throws does he get if he plays in 80% of the 20 games the team plays?"""
    # Define the free throw percentage and number of fouls per game
    free_throw_percentage = 0.7
    fouls_per_game = 5

    # Calculate the total number of games played
    total_games = 20

    # Calculate the number of games John plays in
    games_played = total_games * 0.8

    # Calculate the total number of fouls John gets
    total_fouls = games_played * fouls_per_game

    # Calculate the total number of free throws John gets
    free_throws = total_fouls * 2 * free_throw_percentage

    # Return the result
    result = free_throws
    return result

print(solution())