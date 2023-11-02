def solution():
    
    first_game_points = 10
    second_game_points = 14
    third_game_points = 6
    fourth_game_points = (first_game_points + second_game_points + third_game_points) / 3
    total_points = first_game_points + second_game_points + third_game_points + fourth_game_points
    result = total_points
    return result

print(solution())