def solution():
    # Calculate the number of goals scored by team A in the first half
    goals_A_first_half = 4

    # Calculate the number of goals scored by team B in the first half
    goals_B_first_half = goals_A_first_half - 2

    # Calculate the number of goals scored by team A in the second half
    goals_A_second_half = goals_B_first_half / 4

    # Calculate the total number of goals scored in the match
    total_goals = goals_A_first_half + goals_B_first_half + goals_A_second_half
    result = total_goals
    return result

print(solution())