def solution():
    """Team Soccer Stars plays in a soccer league. They played a total of 20 games, and won 14 games, lost 2, and drew the rest of the matches. They earn 3 points for a win, 1 point for a draw, and nothing for a loss. How many points did they have at the end of the season?"""
    # Define the number of games won, lost, and drawn
    games_won = 14
    games_lost = 2
    games_drawn = 20 - games_won - games_lost

    # Calculate the total number of points earned
    total_points = games_won * 3 + games_drawn * 1

    # Display the total number of points earned
    result = total_points
    return result

print(solution())