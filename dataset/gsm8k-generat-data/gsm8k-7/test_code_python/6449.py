def solution():
    carter_goals = 4
    shelby_goals = carter_goals / 2
    judah_goals = 2 * shelby_goals - 3

    # Calculate the total number of goals scored per game by the team
    total_goals = carter_goals + shelby_goals + judah_goals

    # Calculate the average total number of goals scored per game by the team
    avg_total_goals = total_goals / 3
    result = avg_total_goals
    return result

print(solution())