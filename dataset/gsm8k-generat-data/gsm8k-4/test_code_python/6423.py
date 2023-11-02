def solution():
    """A basketball team won 35 out of the 50 games that they have played. They still have 25 games left to play for the season. How many of the remaining games must they win so that their percentage of wins in the entire season is 64%?"""
    # Define the number of games played and the number of games won
    games_played = 50
    games_won = 35

    # Define the target percentage of wins for the entire season
    target_percentage = 0.64

    # Calculate the total number of games in the season
    total_games = games_played + 25

    # Calculate the number of games the team needs to win in the remaining season to achieve the target percentage
    remaining_wins = round((total_games * target_percentage) - games_won)

    result = remaining_wins
    return result

print(solution())