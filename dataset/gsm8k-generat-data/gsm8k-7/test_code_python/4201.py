def solution():
    losing_team_q1_pts = 10
    winning_team_q1_pts = losing_team_q1_pts * 2

    # Calculate the winning team's points at the end of the second quarter
    winning_team_q2_pts = winning_team_q1_pts + 10

    # Calculate the winning team's points at the end of the third quarter
    winning_team_q3_pts = winning_team_q2_pts + 20

    # Calculate the winning team's points in the fourth quarter
    total_winning_team_pts = 80
    winning_team_q4_pts = total_winning_team_pts - winning_team_q3_pts

    result = winning_team_q4_pts
    return result

print(solution())