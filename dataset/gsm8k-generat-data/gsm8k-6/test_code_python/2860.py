def solution():
    # Calculate the total number of slices of pizza Mr. Mitchell bought
    total_slices = 6 * 12  # 6 pizzas, each with 12 slices

    # Calculate the total number of goals the team scored on the season
    total_goals = total_slices  # one slice for every goal scored

    # Calculate the average number of goals scored per game
    goals_per_game = total_goals / 8  # 8 games in the season
    result = goals_per_game
    return result

print(solution())