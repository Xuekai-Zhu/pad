def solution():
    
    total_players = 24
    total_goals = 150
    total_games = 15

    
    num_players_with_1_goal_per_game = total_players // 3
    goals_from_players_with_1_goal_per_game = num_players_with_1_goal_per_game * total_games

    
    goals_from_other_players = total_goals - goals_from_players_with_1_goal_per_game

    result = goals_from_other_players
    return result

print(solution())