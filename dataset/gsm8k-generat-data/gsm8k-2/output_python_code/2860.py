def solution():
    """The Giants baseball team is trying to make their league playoff. They have played 20 games and won 12 of them. To make the playoffs, they need to win 2/3 of their games over the season. If there are 10 games left, how many do they have to win to make the playoffs?"""
    total_games = 30
    win_goal = 2/3
    current_wins = 12
    remaining_games = 10
    remaining_wins_needed = round((total_games*win_goal) - current_wins)
    playoffs_wins_needed = remaining_wins_needed - remaining_games
    result = playoffs_wins_needed
    return result

print(solution())