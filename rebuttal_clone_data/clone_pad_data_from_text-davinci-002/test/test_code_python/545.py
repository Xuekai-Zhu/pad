def solution():
    points_for_win = 3
    points_for_tie = 1
    joes_team_wins = 1
    joes_team_draws = 3
    first_place_team_wins = 2
    first_place_team_draws = 2
    joes_team_points = (joes_team_wins * points_for_win) + (joes_team_draws * points_for_tie)
    first_place_team_points = (first_place_team_wins * points_for_win) + (first_place_team_draws * points_for_tie)
    points_difference = first_place_team_points - joes_team_points
    result = points_difference
    return result

print(solution())