def solution():
    total_players = 24
    players_scoring_one_goal_per_game = total_players / 3
    games_played = 15
    goals_scored = 150
    goals_scored_by_other_players = goals_scored - (players_scoring_one_goal_per_game * games_played)
    result = goals_scored_by_other_players
    return result

print(solution())