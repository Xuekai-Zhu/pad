def solution():
    # Joe's team
    joes_wins = 1
    joes_draws = 3
    joes_points = (joes_wins * 3) + (joes_draws * 1)

    # First place team
    first_place_wins = 2
    first_place_draws = 2
    first_place_points = (first_place_wins * 3) + (first_place_draws * 1)

    # Difference in points between first place team and Joe's team
    point_difference = first_place_points - joes_points

    result = point_difference
    return result

print(solution())