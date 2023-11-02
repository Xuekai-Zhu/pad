def solution():
    # Calculate the number of points that Team B scored in the first half
    team_b_first_half = 8 / 2

    # Calculate the number of points that Team A scored in the second half
    team_a_second_half = 8 - 2

    # Calculate the number of points that Team B scored in the second half
    team_b_second_half = 8

    # Calculate the total number of points scored by both teams
    total_points = 8 + team_b_first_half + team_a_second_half + team_b_second_half

    # Convert the total number of points to the number of goals
    total_goals = total_points / 2

    result = total_goals
    return result

print(solution())