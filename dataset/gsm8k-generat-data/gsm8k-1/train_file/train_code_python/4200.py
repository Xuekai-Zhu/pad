def solution():
    """At the end of the first quarter, the winning team had double the points of the losing team. At the end of the second quarter, the winning team had 10 more points than it started with. At the end of the third quarter, the winning team had 20 more points than the number it had in the second quarter. If the total points the winning team scored in the game was 80, and the losing team had 10 points in the first quarter, calculate the total number of points the team scored in the fourth quarter."""
    losing_team_points = 10
    first_quarter_points = losing_team_points * 2
    second_quarter_points = first_quarter_points + 10
    third_quarter_points = second_quarter_points + 20
    total_points = 80
    winning_team_points = total_points - losing_team_points
    points_in_fourth_quarter = total_points - first_quarter_points - second_quarter_points - third_quarter_points
    result = points_in_fourth_quarter
    return result

print(solution())