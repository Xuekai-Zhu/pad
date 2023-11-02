def solution():
    # Calculate the total number of points he wants to score in the season
    total_points_wanted = 30 * 20  # he wants to average 30 points throughout the 20 game season
    total_points_so_far = 26 * 15  # he has already scored 26 points in each of the 15 games

    # Calculate the average points he needs to score in the remaining games
    remaining_games = 20 - 15
    points_needed_per_game = (total_points_wanted - total_points_so_far) / remaining_games
    result = points_needed_per_game
    return result

print(solution())