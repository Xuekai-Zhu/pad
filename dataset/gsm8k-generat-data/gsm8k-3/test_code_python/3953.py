def solution():
    """
    The number of goals scored in a game against Barca by exactly two players last season accounts for 20% of all goals scored in the league.
    If the players scored an equal number of goals, and the total number of goals scored in the league against Barca that season is 300,
    calculate the number of goals each of the two players scored.
    """
    # Calculate the total number of goals scored by the two players in the game against Barca
    barca_goals = 0.2 * 300
    player_goals = barca_goals / 2

    # Display the number of goals each player scored
    result = player_goals
    return result

print(solution())