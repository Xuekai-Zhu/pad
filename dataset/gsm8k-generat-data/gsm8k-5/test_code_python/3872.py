def solution():
    first_away_game = x  # Let's assume the first away game scored x points
    home_game = 2 * first_away_game  # The home game scored twice as many points as the first away game
    second_away_game = first_away_game + 18  # The second away game scored 18 more points than the first
    third_away_game = second_away_game + 2  # The third away game scored 2 more points than the second
    total_points = home_game + first_away_game + second_away_game + third_away_game  # Calculate the total points
    desired_points = 4 * 62  # The team wants to score 4 times as many points as their last home game
    next_game_points = desired_points - total_points  # Calculate the remaining points needed in the next game
    result = next_game_points
    return result

print(solution())