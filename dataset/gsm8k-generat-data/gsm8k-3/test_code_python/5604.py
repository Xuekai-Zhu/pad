def solution():
    """During a soccer game, in the first half, Team A scored 8 points, and Team B scored only half as many points. In the second half, Team B was able to get as many points as Team A in the first half, and Team A scored only 2 goals less than Team B. How many goals did both teams score during the whole match?"""
    # Calculate the number of goals scored by Team B in the first half
    team_b_first_half = 8 / 2

    # Calculate the number of goals scored by Team A in the second half
    team_a_second_half = team_b_first_half

    # Calculate the number of goals scored by Team B in the second half
    team_b_second_half = 8 - 2

    # Calculate the total number of goals scored by both teams
    total_goals = 8 + team_b_first_half + team_a_second_half + team_b_second_half

    # Display the total number of goals
    result = total_goals
    return result

print(solution())