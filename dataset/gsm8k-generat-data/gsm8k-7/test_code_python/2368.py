def solution():
    game1_points = 10
    game2_points = 14
    game3_points = 6

    # Calculate the average of Clayton's points from the first three games
    avg_points = (game1_points + game2_points + game3_points) / 3

    game4_points = avg_points

    # Calculate the total points scored by Clayton in the first four games
    total_points = game1_points + game2_points + game3_points + game4_points
    result = total_points
    return result

print(solution())