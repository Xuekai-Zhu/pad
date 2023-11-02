def solution():
    """The Giants baseball team is trying to make their league playoff. They have played 20 games and won 12 of them. To make the playoffs, they need to win 2/3 of their games over the season. If there are 10 games left, how many do they have to win to make the playoffs?"""
    # Define the number of games played and won so far
    games_played = 20
    games_won = 12

    # Define the number of games remaining
    games_remaining = 10

    # Calculate the number of games the team needs to win to meet the 2/3 requirement
    games_needed = round((games_played + games_remaining) * (2/3)) - games_won

    # Display the number of games the team needs to win
    result = games_needed
    return result

print(solution())