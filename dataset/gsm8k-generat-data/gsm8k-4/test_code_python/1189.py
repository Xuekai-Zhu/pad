def solution():
    """Yolanda scored 345 points over the entire season. There were 15 games over the season. She averaged 4 free throws (worth one point), and 5 two-point baskets per game. How many three-point baskets did she average a game?"""
    # Define the total number of points scored and the total number of baskets made
    total_points = 345
    total_baskets = 15 * (4 + 5 * 2)  # 4 free throws and 5 two-point baskets per game

    # Calculate the number of three-point baskets made
    three_point_baskets = (total_points - total_baskets) / 3

    # Calculate the average number of three-point baskets per game
    per_game_avg = three_point_baskets / 15

    # Return the result
    result = per_game_avg
    return result

print(solution())