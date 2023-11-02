def solution():
    """Mr. Mitchell is buying pizzas for the soccer team. He buys one slice for every goal they scored on the season. A large pizza has 12 slices. If he bought 6 pizzas, and the team had 8 games, how many goals did they score per game on average?"""
    total_slices = 6 * 12
    games_played = 8
    goals_scored = total_slices / games_played
    result = goals_scored
    return result

print(solution())