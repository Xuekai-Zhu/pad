def solution():
    # Calculate the total cost of the game with tax
    game_cost = 50 * 1.1

    # Calculate Nina's savings per week
    weekly_savings = 10 / 2

    # Calculate the number of weeks needed to save up for the game
    num_weeks = game_cost / weekly_savings
    result = num_weeks
    return result

print(solution())