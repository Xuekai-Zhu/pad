def solution():
    """At the end of the first quarter, the winning team had double the points of the losing team. At the end of the second quarter, the winning team had 10 more points than it started with. At the end of the third quarter, the winning team had 20 more points than the number it had in the second quarter. If the total points the winning team scored in the game was 80, and the losing team had 10 points in the first quarter, calculate the total number of points the team scored in the fourth quarter."""
    # Determine the number of points the winning team had in the first quarter
    losing_team_points = 10
    winning_team_points_1 = losing_team_points * 2

    # Determine the number of points the winning team had in the second quarter
    winning_team_points_2 = winning_team_points_1 + 10

    # Determine the number of points the winning team had in the third quarter
    winning_team_points_3 = winning_team_points_2 + 20

    # Determine the total number of points the winning team scored in the game
    winning_team_points_total = 80

    # Determine the number of points the winning team had in the fourth quarter
    winning_team_points_4 = winning_team_points_total - winning_team_points_3

    # Display the number of points the winning team had in the fourth quarter
    result = winning_team_points_4
    return result

print(solution())