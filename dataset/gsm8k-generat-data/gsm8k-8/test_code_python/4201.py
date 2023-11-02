def solution():
    # Calculate the number of points the winning team had at the end of the first quarter
    winning_team_q1 = 10 + (2 * 10)  # 30 points

    # Calculate the number of points the winning team had at the end of the second quarter
    winning_team_q2 = winning_team_q1 + 10  # 40 points

    # Calculate the number of points the winning team had at the end of the third quarter
    winning_team_q3 = winning_team_q2 + 20  # 60 points

    # Calculate the number of points the winning team scored in the fourth quarter
    winning_team_q4 = 80 - winning_team_q3 - 10 - 10  # 0 points (since the losing team had 10 points in the first quarter)
    result = winning_team_q4
    return result

print(solution())