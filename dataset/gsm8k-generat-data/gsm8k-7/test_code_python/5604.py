def solution():
    team_a_first_half = 8
    team_b_first_half = team_a_first_half / 2

    team_a_second_half = team_b_first_half + 2
    team_b_second_half = team_a_first_half

    total_goals = team_a_first_half + team_b_first_half + team_a_second_half + team_b_second_half
    result = total_goals
    return result

print(solution())