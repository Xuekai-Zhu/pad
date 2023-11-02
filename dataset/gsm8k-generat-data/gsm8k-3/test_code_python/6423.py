def solution():
    """A basketball team won 35 out of the 50 games that they have played. They still have 25 games left to play for the season. How many of the remaining games must they win so that their percentage of wins in the entire season is 64%?"""
    # Define the number of games played and the desired win percentage
    games_played = 50 + 25
    desired_percentage = 0.64

    # Calculate the number of games the team needs to win to achieve the desired percentage
    wins_needed = round(games_played * desired_percentage) - 35

    # Calculate the number of wins needed in the remaining games
    remaining_wins_needed = max(0, wins_needed - 25)

    # Display the number of remaining wins needed
    result = remaining_wins_needed
    return result

print(solution())