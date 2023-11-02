def solution():
    # Calculate the average number of goals scored per game by the team
    carter_goals = 4
    shelby_goals = 0.5 * carter_goals
    judah_goals = 2 * shelby_goals - 3
    total_goals = carter_goals + shelby_goals + judah_goals
    avg_goals_per_game = total_goals / 3
    result = avg_goals_per_game
    return result

print(solution())