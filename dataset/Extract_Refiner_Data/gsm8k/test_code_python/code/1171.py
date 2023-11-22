def solution():
    
    # Define the number of goals scored by team A in the first half
    team_a_goals = 4

    # Define the number of goals scored by team B in the first half
    team_b_goals = team_a_goals - 2

    # Define the number of goals scored by team A in the second half
    team_a_goals_second_half = team_b_goals * 0.25

    # Calculate the total number of goals scored in the match
    total_goals = team_a_goals + team_b_goals + team_a_goals_second_half

    # Display the total number of goals scored
    result = total_goals
    return result

print(solution())