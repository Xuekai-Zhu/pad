def solution():
    
    total_points = 345
    games_played = 15
    free_throws_per_game = 4
    two_point_baskets_per_game = 5
    points_from_free_throws = free_throws_per_game * games_played
    points_from_two_point_baskets = two_point_baskets_per_game * 2 * games_played
    points_from_three_point_baskets = total_points - points_from_free_throws - points_from_two_point_baskets
    three_point_baskets_per_game = points_from_three_point_baskets / (games_played * 3)
    result = three_point_baskets_per_game
    return result

print(solution())