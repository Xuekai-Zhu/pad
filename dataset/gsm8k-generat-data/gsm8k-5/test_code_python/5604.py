def solution():
    team_a_first_half = 8  # Team A scored 8 points in the first half
    team_b_first_half = team_a_first_half / 2  # Team B scored half as many points as Team A in the first half
    team_a_second_half = team_b_first_half  # Team B scored as many points as Team A in the first half
    team_b_second_half = team_a_first_half - 2  # Team A scored 2 goals less than Team B in the second half

    # Calculate the total number of goals scored by both teams
    total_goals = team_a_first_half + team_b_first_half + team_a_second_half + team_b_second_half
    result = total_goals
    return result

print(solution())