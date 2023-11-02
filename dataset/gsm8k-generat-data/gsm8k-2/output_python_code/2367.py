def solution():
    """Clayton plays basketball on a team. He has played three games so far. In the first game, he scored 10 points. In the second game, he scored 14 points. In the third game, he scored 6 points. In the fourth game, he scored the average of his points from the first three games. How many total points did Clayton score during the first four games?"""
    first_game_points = 10
    second_game_points = 14
    third_game_points = 6
    fourth_game_points = (first_game_points + second_game_points + third_game_points) / 3
    total_points = first_game_points + second_game_points + third_game_points + fourth_game_points
    result = total_points
    return result

print(solution())