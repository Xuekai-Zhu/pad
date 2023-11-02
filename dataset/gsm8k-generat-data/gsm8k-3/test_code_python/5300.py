def solution():
    """Javier plays 2 baseball games a week. In each of his first 20 games, he averaged 2 hits. If he has 10 games left, how many hits a game does he have to average to bring his average for the season up to 3 hits a game?"""
    # Define the number of games played and the current average hits per game
    games_played = 20
    current_average = 2

    # Define the target average hits per game
    target_average = 3

    # Define the number of games left
    games_left = 10

    # Calculate the total number of hits needed to reach the target average
    total_hits_needed = (target_average * (games_played + games_left)) - (current_average * games_played)

    # Calculate the average hits needed per game for the remaining games
    average_hits_needed = total_hits_needed / games_left

    # Display the average hits needed
    result = average_hits_needed
    return result

print(solution())