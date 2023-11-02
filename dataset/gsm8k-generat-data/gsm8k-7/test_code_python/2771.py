def solution():
    hours_played = 2
    points_per_minute = 1/5
    points_needed_to_win = 8

    # Calculate the total number of points Jeff scores in 2 hours
    total_points_scored = points_per_minute * 60 * hours_played

    # Calculate the total number of games Jeff won
    total_games_won = total_points_scored // points_needed_to_win
    result = total_games_won
    return result

print(solution())