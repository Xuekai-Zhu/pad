def solution():
    """Malik rushed for 18 yards in each of 4 games. Josiah ran for 22 yards in each of 4 games. Darnell had an average of 11 yards rushed for each of the 4 games. How many yards did the 3 athletes run in total?"""
    # Define the number of games played
    num_games = 4

    # Calculate the total yards rushed by Malik and Josiah
    malik_yards = 18 * num_games
    josiah_yards = 22 * num_games
    total_yards = malik_yards + josiah_yards

    # Calculate the total yards rushed by Darnell
    darnell_yards = 11 * num_games

    # Add the total yards of all three athletes
    total_yards += darnell_yards

    # Return the result
    result = total_yards
    return result

print(solution())