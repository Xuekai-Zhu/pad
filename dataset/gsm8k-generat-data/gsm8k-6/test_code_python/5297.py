def solution():
    # Calculate the number of players who have averaged 1 goal each per game
    players_goal = 24 * (1/3)
    # Calculate the total number of goals scored by these players
    players_goal_total = players_goal * 1 * 15  # 1 goal per game, 15 games played
    # Calculate the total number of goals scored by the other players
    other_players_goal_total = 150 - players_goal_total
    result = other_players_goal_total
    return result

print(solution())