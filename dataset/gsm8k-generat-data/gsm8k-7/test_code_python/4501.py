def solution():
    first_game_points = 30
    second_game_points = first_game_points / 2
    third_game_points = second_game_points * 3
    roosevelt_total_points = first_game_points + second_game_points + third_game_points + 50
    greendale_total_points = roosevelt_total_points - 10
    greendale_points = greendale_total_points - (first_game_points + second_game_points + third_game_points)
    result = greendale_points
    return result

print(solution())