def solution():
    """In the first half of a soccer match, team A scores 4 goals while team B scores 2 goals fewer than team A. In the second half, team A scores 1/4 of the number of goals scored by team B, which scores 4 times the number of goals it scored in the first half. What's the total number of goals scored in the match?"""
    goals_teamA_first = 4
    goals_teamB_first = goals_teamA_first - 2
    goals_teamB_second = 4 * goals_teamB_first
    goals_teamA_second = goals_teamB_second / 4
    total_goals = goals_teamA_first + goals_teamB_first + goals_teamA_second + goals_teamB_second
    result = total_goals
    return result

print(solution())