def solution():
    # Calculate Carter's average goals per game
    carter_goals = 4

    # Calculate Shelby's average goals per game (half as many as Carter)
    shelby_goals = carter_goals / 2

    # Calculate Judah's average goals per game (3 less than twice as many as Shelby)
    judah_goals = 2 * shelby_goals - 3

    # Calculate the average total number of goals scored by the team per game
    average_goals = carter_goals + shelby_goals + judah_goals

    result = average_goals
    return result

print(solution())