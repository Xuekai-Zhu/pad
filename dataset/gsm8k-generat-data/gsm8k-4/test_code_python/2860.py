def solution():
    """Mr. Mitchell is buying pizzas for the soccer team.
    He buys one slice for every goal they scored on the season.
    A large pizza has 12 slices. If he bought 6 pizzas, and the team had 8 games,
    how many goals did they score per game on average?"""
    # Calculate the total number of slices bought
    total_slices = 6 * 12

    # Calculate the total number of goals scored
    total_goals = total_slices

    # Calculate the average number of goals per game
    goals_per_game = total_goals / 8

    # return the result
    result = goals_per_game
    return result

print(solution())