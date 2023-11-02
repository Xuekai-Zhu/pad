def solution():
    """Clayton plays basketball on a team. He has played three games so far. In the first game, he scored 10 points. In the second game, he scored 14 points. In the third game, he scored 6 points. In the fourth game, he scored the average of his points from the first three games. How many total points did Clayton score during the first four games?"""
    # Define the points scored in each game
    game1 = 10
    game2 = 14
    game3 = 6

    # Calculate the average of points from the first three games
    avg_points = (game1 + game2 + game3) / 3

    # Calculate the total points scored in the first four games
    total_points = game1 + game2 + game3 + avg_points

    result = total_points
    return result

print(solution())