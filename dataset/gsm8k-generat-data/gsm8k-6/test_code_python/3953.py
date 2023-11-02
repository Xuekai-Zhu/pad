def solution():
    # Calculate the number of goals scored by the two players
    total_goals = 300  # total number of goals scored in the league against Barca
    two_players_goals = 0.2 * total_goals  # number of goals scored by the two players
    each_player_goals = two_players_goals / 2  # since the players scored an equal number of goals
    result = each_player_goals
    return result

print(solution())