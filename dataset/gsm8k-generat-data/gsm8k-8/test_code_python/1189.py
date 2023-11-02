def solution():
    # Calculate Yolanda's total points scored per game
    total_points_per_game = 345 / 15

    # Calculate the total points scored from free throws per game
    free_throw_points_per_game = 4

    # Calculate the total points scored from two-point baskets per game
    two_point_basket_points_per_game = total_points_per_game - free_throw_points_per_game

    # Calculate the number of two-point baskets per game
    num_two_point_baskets_per_game = 5

    # Calculate the total points scored from three-point baskets per game
    total_points_from_three_pointers_per_game = two_point_basket_points_per_game - (2*num_two_point_baskets_per_game)

    # Calculate the number of three-point baskets per game
    num_three_point_baskets_per_game = total_points_from_three_pointers_per_game / 3

    result = num_three_point_baskets_per_game
    return result

print(solution())