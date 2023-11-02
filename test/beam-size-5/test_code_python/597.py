def solution():
    
    # Define the number of games Steve buys each year
    games_per_year_1 = 1
    games_per_year_2 = 2
    games_per_year_3 = 4

    # Define the number of games Steve gets for Christmas each year
    games_for_christmas = 5

    # Calculate the total number of games Steve has after 3 years
    total_games = (games_per_year_1 * 12) + (games_per_year_2 * 12) + (games_per_year_3 * 12) + games_for_christmas

    # Display the total number of games
    result = total_games
    return result

print(solution())