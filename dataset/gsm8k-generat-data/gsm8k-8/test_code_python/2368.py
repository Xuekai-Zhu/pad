def solution():
    # Calculate the average of Clayton's points from the first three games
    avg_first_three_games = (10 + 14 + 6) / 3

    # Calculate Clayton's points from the fourth game
    points_fourth_game = avg_first_three_games

    # Calculate Clayton's total points from all four games
    total_points = 10 + 14 + 6 + points_fourth_game
    result = total_points
    return result

print(solution())