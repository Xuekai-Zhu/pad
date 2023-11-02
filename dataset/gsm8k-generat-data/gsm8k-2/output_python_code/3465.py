def solution():
    """UF got into the national championship. For them to get into the championship, they scored a total of 720 points during their previous 24 games. In the championship game, however, their opponent was much stronger than any other team they had previously gone against and they scored 2 points less than half as much as they had previously scored in each of the 24 games. Their opponent only lost by 2 points. How many points did their opponent score?"""
    previous_games_points = 720
    previous_games_average = previous_games_points / 24
    championship_game_score = (previous_games_average / 2) - 2
    opponent_score = championship_game_score + 2
    result = opponent_score
    return result

print(solution())