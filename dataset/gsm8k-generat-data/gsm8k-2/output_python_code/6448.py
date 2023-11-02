def solution():
    """Carter plays soccer on the school team. On average, he scores 4 goals per game. Shelby scores half as many as Carter per game on average. And Judah, on average, scores three less than twice as many goals per game as Shelby. If these three teammates are the only ones that score goals for the school team, what is the average total number of goals scored by the team per game?"""
    carter_goals = 4
    shelby_goals = carter_goals / 2
    judah_goals = (2 * shelby_goals) - 3
    total_goals = carter_goals + shelby_goals + judah_goals
    average_goals = total_goals / 3
    result = average_goals
    return result

print(solution())