def solution():
    carter_goals_per_game = 4
    shelby_goals_per_game = carter_goals_per_game / 2
    judah_goals_per_game = (2 * shelby_goals_per_game) - 3

    # Calculate the average total number of goals scored by the team per game
    avg_total_goals_per_game = carter_goals_per_game + shelby_goals_per_game + judah_goals_per_game
    result = avg_total_goals_per_game
    return result

print(solution())