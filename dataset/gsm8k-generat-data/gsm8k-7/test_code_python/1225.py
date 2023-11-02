def solution():
    current_average = 26
    total_games = 20
    current_games_played = 15
    goal_average = 30

    # Calculate the total points Donovan needs to score to reach his goal
    total_points_goal = goal_average * total_games

    # Calculate the total points Donovan has scored so far
    total_points_current = current_average * current_games_played

    # Calculate the remaining points Donovan needs to score
    remaining_points = total_points_goal - total_points_current

    # Calculate the average points Donovan needs to score per game to reach his goal
    average_per_game = remaining_points / (total_games - current_games_played)

    result = average_per_game
    return result

print(solution())