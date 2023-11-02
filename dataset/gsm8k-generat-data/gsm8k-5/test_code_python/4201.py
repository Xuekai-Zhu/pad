def solution():
    losing_points_q1 = 10  # The losing team had 10 points in the first quarter
    total_points_winning_team = 80  # The winning team scored a total of 80 points in the game

    # Calculate the points scored by the winning team in the first quarter
    winning_points_q1 = 2 * losing_points_q1  # The winning team had double the points of the losing team in the first quarter

    # Calculate the points scored by the winning team in the second quarter
    winning_points_q2 = winning_points_q1 + 10  # The winning team had 10 more points than it started with in the second quarter

    # Calculate the points scored by the winning team in the third quarter
    winning_points_q3 = winning_points_q2 + 20  # The winning team had 20 more points than the number it had in the second quarter in the third quarter

    # Calculate the points scored by the winning team in the fourth quarter
    winning_points_q4 = total_points_winning_team - (winning_points_q1 + winning_points_q2 + winning_points_q3)  # The total points scored by the winning team minus the points scored in the first three quarters

    result = winning_points_q4
    return result

print(solution())