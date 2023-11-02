def solution():
    """The Giants baseball team is trying to make their league playoff. They have played 20 games and won 12 of them. To make the playoffs, they need to win 2/3 of their games over the season. If there are 10 games left, how many do they have to win to make the playoffs?"""
    total_games = 30
    games_played = 20
    games_left = 10
    needed_wins = (2/3 * total_games) - games_played
    remaining_wins = needed_wins - games_left
    result = remaining_wins
    
    return result

print(solution())