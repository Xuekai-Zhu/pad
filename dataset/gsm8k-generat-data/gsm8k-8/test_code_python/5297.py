def solution():
    total_players = 24
    total_goals = 150
    total_games = 15
    one_third = total_players // 3
    one_goal_players = one_third
    total_one_goal_players_goals = one_goal_players * total_games
    total_other_players_goals = total_goals - total_one_goal_players_goals
    result = total_other_players_goals
    return result

print(solution())