def solution():
    """Javier plays 2 baseball games a week. In each of his first 20 games, he averaged 2 hits. If he has 10 games left, how many hits a game does he have to average to bring his average for the season up to 3 hits a game?"""
    # Define the total number of games and hits he needs to achieve his goal
    total_games = 30
    total_hits_needed = total_games * 3 - 40

    # Calculate the number of hits he needs to average in his remaining games
    remaining_games = 10
    remaining_hits_needed = total_hits_needed / remaining_games

    # Display the result
    result = remaining_hits_needed
    return result

print(solution())