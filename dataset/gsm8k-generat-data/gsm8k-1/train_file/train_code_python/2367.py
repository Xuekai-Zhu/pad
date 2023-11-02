def solution():
    """Clayton plays basketball on a team. He has played three games so far. In the first game, he scored 10 points. In the second game, he scored 14 points. In the third game, he scored 6 points. In the fourth game, he scored the average of his points from the first three games. How many total points did Clayton score during the first four games?"""
    game_1 = 10
    game_2 = 14
    game_3 = 6
    game_4 = (game_1 + game_2 + game_3) / 3
    total_points = game_1 + game_2 + game_3 + game_4
    result = total_points
    return result

print(solution())