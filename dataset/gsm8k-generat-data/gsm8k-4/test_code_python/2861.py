def solution():
    """The Giants baseball team is trying to make their league playoff. They have played 20 games and won 12 of them. To make the playoffs, they need to win 2/3 of their games over the season. If there are 10 games left, how many do they have to win to make the playoffs?"""
    # Define the number of games already played and number of games left
    games_played = 20
    games_left = 10

    # Define the target win percentage needed to make the playoffs
    target_win_percentage = 2/3

    # Calculate the total number of games in the season
    total_games = games_played + games_left

    # Calculate the minimum number of games the Giants need to win to make the playoffs
    min_wins = total_games * target_win_percentage - games_played

    # Round up to the nearest whole number
    min_wins = int(math.ceil(min_wins))

    # Ensure that the minimum number of wins is at least 0
    min_wins = max(0, min_wins)

    # Return the result
    result = min_wins
    return result

print(solution())