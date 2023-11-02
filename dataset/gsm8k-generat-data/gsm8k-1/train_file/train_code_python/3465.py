def solution():
    """UF got into the national championship. For them to get into the championship, they scored a total of 720 points during their previous 24 games. In the championship game, however, their opponent was much stronger than any other team they had previously gone against and they scored 2 points less than half as much as they had previously scored in each of the 24 games. Their opponent only lost by 2 points. How many points did their opponent score?"""
    total_points = 720
    games_played = 24
    average_points_per_game = total_points / games_played
    opponent_score = (average_points_per_game / 2) - 2
    result = opponent_score
    return result

print(solution())