def solution():
    """At the end of the first quarter, the winning team had double the points of the losing team. At the end of the second quarter, the winning team had 10 more points than it started with. At the end of the third quarter, the winning team had 20 more points than the number it had in the second quarter. If the total points the winning team scored in the game was 80, and the losing team had 10 points in the first quarter, calculate the total number of points the team scored in the fourth quarter."""
    # Define the initial points of the winning and losing team
    losing_team_q1_points = 10
    winning_team_q1_points = 2 * losing_team_q1_points

    # Calculate the points of the winning team at the end of the second quarter
    winning_team_q2_points = winning_team_q1_points + 10

    # Calculate the points of the winning team at the end of the third quarter
    winning_team_q3_points = winning_team_q2_points + 20

    # Calculate the total points of the winning team in the game
    total_winning_points = 80

    # Calculate the points of the winning team in the fourth quarter
    winning_team_q4_points = total_winning_points - winning_team_q3_points

    # Calculate the total points of the winning team
    total_points = winning_team_q1_points + winning_team_q2_points + winning_team_q3_points + winning_team_q4_points

    result = winning_team_q4_points
    return result

print(solution())