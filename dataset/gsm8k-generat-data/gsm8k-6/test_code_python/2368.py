def solution():
    # Calculate the total points Clayton scored in the first three games
    total_points_first_three_games = 10 + 14 + 6

    # Calculate the average points per game in the first three games
    avg_points_first_three_games = total_points_first_three_games / 3

    # Calculate the total points Clayton scored in the first four games
    total_points_first_four_games = total_points_first_three_games + avg_points_first_three_games

    result = total_points_first_four_games
    return result

print(solution())