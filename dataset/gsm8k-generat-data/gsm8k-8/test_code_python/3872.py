def solution():
    # Define the points scored in the last home game
    last_home_game = 62

    # Calculate the points scored in the first away game
    first_away_game = last_home_game // 2

    # Calculate the points scored in the second away game
    second_away_game = first_away_game + 18

    # Calculate the points scored in the third away game
    third_away_game = second_away_game + 2

    # Calculate the total points scored so far
    total_points = last_home_game + first_away_game + second_away_game + third_away_game

    # Calculate the points needed in the next game to reach the target of 4 times the last home game score
    target_points = 4 * last_home_game
    next_game_points = target_points - total_points

    result = next_game_points
    return result

print(solution())