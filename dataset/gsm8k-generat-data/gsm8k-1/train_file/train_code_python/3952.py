def solution():
    """The number of goals scored in a game against Barca by exactly two players last season accounts for 20% of all goals scored in the league. If the players scored an equal number of goals, and the total number of goals scored in the league against Barca that season is 300, calculate the number of goals each of the two players scored."""
    total_goals = 300
    goals_by_two_players = total_goals * 0.2
    goals_per_player = goals_by_two_players / 2
    result = goals_per_player
    return result

print(solution())