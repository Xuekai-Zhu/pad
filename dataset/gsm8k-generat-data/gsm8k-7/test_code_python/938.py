def solution():
    # Joe's team
    joe_wins = 1
    joe_draws = 3
    joe_points = (joe_wins * 3) + (joe_draws * 1)

    # First-place team
    first_place_wins = 2
    first_place_draws = 2
    first_place_points = (first_place_wins * 3) + (first_place_draws * 1)

    # Calculate the difference in points between first place team and Joe's team
    point_difference = first_place_points - joe_points
    result = point_difference
    return result

print(solution())