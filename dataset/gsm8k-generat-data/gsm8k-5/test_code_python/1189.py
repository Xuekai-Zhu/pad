def solution():
    total_points = 345  # Yolanda scored a total of 345 points over the season
    num_games = 15  # There were 15 games over the season
    num_free_throws = 4  # Yolanda averaged 4 free throws per game, worth 1 point each
    num_two_point_baskets = 5  # Yolanda averaged 5 two-point baskets per game, worth 2 points each

    # Calculate the number of points Yolanda scored from free throws over the season
    free_throw_points = num_free_throws * num_games

    # Calculate the number of points Yolanda scored from two-point baskets over the season
    two_point_basket_points = num_two_point_baskets * 2 * num_games

    # Calculate the number of points Yolanda scored from three-point baskets over the season
    three_point_basket_points = total_points - free_throw_points - two_point_basket_points

    # Calculate the average number of three-point baskets Yolanda made per game
    avg_three_point_baskets = three_point_basket_points / (num_games * 3)

    result = avg_three_point_baskets
    return result

print(solution())