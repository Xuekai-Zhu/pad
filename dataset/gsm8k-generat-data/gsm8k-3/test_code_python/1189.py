def solution():
    """Yolanda scored 345 points over the entire season. There were 15 games over the season. She averaged 4 free throws (worth one point), and 5 two-point baskets per game. How many three-point baskets did she average a game?"""
    # Define the total number of games and points scored
    total_games = 15
    total_points = 345

    # Calculate the total number of free throws and two-point baskets made
    total_free_throws = total_games * 4
    total_two_point_baskets = total_games * 5

    # Calculate the total number of points scored from free throws and two-point baskets
    free_throw_points = total_free_throws
    two_point_points = total_two_point_baskets * 2
    total_points_from_ft_and_tp = free_throw_points + two_point_points

    # Calculate the total number of points scored from three-point baskets
    total_points_from_tp = total_points - total_points_from_ft_and_tp
    total_three_point_baskets = total_points_from_tp / 3

    # Calculate the average number of three-point baskets made per game
    average_three_point_baskets_per_game = total_three_point_baskets / total_games

    # Display the average number of three-point baskets made per game
    result = average_three_point_baskets_per_game
    return result

print(solution())