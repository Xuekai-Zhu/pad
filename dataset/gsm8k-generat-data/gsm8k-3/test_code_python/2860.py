def solution():
    """Mr. Mitchell is buying pizzas for the soccer team. He buys one slice for every goal they scored on the season. A large pizza has 12 slices. If he bought 6 pizzas, and the team had 8 games, how many goals did they score per game on average?"""
    # Define the number of slices in a large pizza
    SLICES_PER_PIZZA = 12

    # Calculate the total number of slices of pizza needed
    slices_needed = 6 * SLICES_PER_PIZZA

    # Calculate the total number of goals scored
    goals_scored = slices_needed

    # Calculate the average number of goals scored per game
    goals_per_game = goals_scored / 8

    # Display the average number of goals scored per game
    result = goals_per_game
    return result

print(solution())