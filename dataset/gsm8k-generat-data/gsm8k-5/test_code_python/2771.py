def solution():
    time_in_minutes = 2 * 60  # Jeff plays for 2 hours, which is 120 minutes
    time_in_5_min_intervals = time_in_minutes // 5  # Convert time to number of 5-minute intervals
    points_per_game = 8  # Jeff wins a match when he scores 8 points

    # Calculate the total number of points Jeff scores in the 2 hours of playtime
    total_points = time_in_5_min_intervals // 3  # Jeff scores a point every 5 minutes, which is 1 point every 3 5-minute intervals

    # Calculate the number of games Jeff wins
    games_won = total_points // points_per_game
    result = games_won
    return result

print(solution())