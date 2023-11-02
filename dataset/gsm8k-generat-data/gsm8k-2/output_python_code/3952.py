def solution():
    """The number of goals scored in a game against Barca by exactly two players last season accounts for 20% of all goals scored in the league. If the players scored an equal number of goals, and the total number of goals scored in the league against Barca that season is 300, calculate the number of goals each of the two players scored."""
    goals_against_barca = 300
    total_goals = goals_against_barca / 0.2
    equal_goals = total_goals / 2
    result = equal_goals
    return result

print(solution())