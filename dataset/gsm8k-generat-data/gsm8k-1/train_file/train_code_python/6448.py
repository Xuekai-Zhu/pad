def solution():
    """Carter plays soccer on the school team. On average, he scores 4 goals per game. Shelby scores half as many as Carter per game on average. And Judah, on average, scores three less than twice as many goals per game as Shelby. If these three teammates are the only ones that score goals for the school team, what is the average total number of goals scored by the team per game?"""
    carter_goals_per_game = 4
    shelby_goals_per_game = carter_goals_per_game / 2
    judah_goals_per_game = (2 * shelby_goals_per_game) - 3
    total_goals_per_game = carter_goals_per_game + shelby_goals_per_game + judah_goals_per_game
    average_goals_per_game = total_goals_per_game / 3
    result = average_goals_per_game
    return result

print(solution())