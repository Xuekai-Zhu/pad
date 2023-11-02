def solution():
    """Mr. Mitchell is buying pizzas for the soccer team. He buys one slice for every goal they scored on the season. A large pizza has 12 slices. If he bought 6 pizzas, and the team had 8 games, how many goals did they score per game on average?"""
    slices_per_pizza = 12
    total_slices = slices_per_pizza * 6
    games_played = 8
    goals_per_game = total_slices / games_played
    result = goals_per_game
    return result

print(solution())