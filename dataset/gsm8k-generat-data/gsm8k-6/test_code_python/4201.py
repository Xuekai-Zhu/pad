def solution():
    # Calculate the winning team's points at the end of each quarter
    losing_team_points = 10  # points scored by the losing team in the first quarter
    winning_team_points_q1 = losing_team_points * 2  # points scored by the winning team in the first quarter
    winning_team_points_q2 = winning_team_points_q1 + 10  # points scored by the winning team in the second quarter
    winning_team_points_q3 = winning_team_points_q2 + 20  # points scored by the winning team in the third quarter
    total_winning_team_points = 80  # total points scored by the winning team in the game

    # Calculate the points scored by the winning team in the fourth quarter
    winning_team_points_q4 = total_winning_team_points - winning_team_points_q3

    result = winning_team_points_q4
    return result

print(solution())