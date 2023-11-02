def solution():
    game1_points = 10
    game2_points = 14
    game3_points = 6
    game4_points = (game1_points + game2_points + game3_points) / 3
    total_points = game1_points + game2_points + game3_points + game4_points
    result = total_points
    return result

print(solution())