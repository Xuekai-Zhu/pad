def solution():
    num_players = 24
    total_goals = 150
    num_games = 15

    # Calculate the total number of goals scored by 1/3 of the players
    num_players_with_1_goal_per_game = num_players / 3
    goals_by_1_goal_per_game_players = num_players_with_1_goal_per_game * num_games

    # Calculate the total number of goals scored by the rest of the players
    goals_by_rest_of_players = total_goals - goals_by_1_goal_per_game_players

    result = goals_by_rest_of_players
    return result

print(solution())