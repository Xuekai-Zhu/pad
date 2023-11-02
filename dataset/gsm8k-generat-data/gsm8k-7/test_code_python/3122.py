def solution():
    matthew_points = 9
    shawn_points = 6
    points_per_basket = 3

    # Calculate the total points scored by both players combined
    total_points = matthew_points + shawn_points

    # Calculate the total number of baskets made
    num_baskets = total_points / points_per_basket
    result = num_baskets
    return result

print(solution())