def solution():
    """The number of goals scored in a game against Barca by exactly two players last season accounts for 20% of all goals scored in the league. If the players scored an equal number of goals, and the total number of goals scored in the league against Barca that season is 300, calculate the number of goals each of the two players scored."""
    # Define the total number of goals scored in the league against Barca
    total_goals = 300

    # Calculate the number of goals scored by the two players combined
    player_goals = total_goals * 0.2

    # Calculate the number of goals scored by each player
    player_goals_each = player_goals / 2

    # Return the result
    result = player_goals_each
    return result

print(solution())