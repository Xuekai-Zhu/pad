def solution():
    # Calculate the total points scored in the first three games
    total_points_first_three = 10 + 14 + 6

    # Calculate the average points score in the first three games
    average_points_first_three = total_points_first_three / 3

    # Calculate the points scored in the fourth game
    points_fourth_game = average_points_first_three

    # Calculate the total points scored in the first four games
    total_points = total_points_first_three + points_fourth_game
    result = total_points
    return result

print(solution())