def solution():
    """John hits 70% of his free throws. For every foul he gets 2 shots. He gets fouled 5 times a game. How many free throws does he get if he plays in 80% of the 20 games the team plays?"""
    # Define the given values
    free_throw_percentage = 0.70
    fouls_per_game = 5
    shots_per_foul = 2
    games_played = 20
    games_played_percentage = 0.80

    # Calculate the total number of fouls John will get in the games he plays
    total_fouls = fouls_per_game * games_played * games_played_percentage

    # Calculate the total number of shots John will take
    total_shots = total_fouls * shots_per_foul

    # Calculate the total number of free throws John will get
    free_throws = total_shots * free_throw_percentage

    # Display the total number of free throws John will get
    result = free_throws
    return result

print(solution())