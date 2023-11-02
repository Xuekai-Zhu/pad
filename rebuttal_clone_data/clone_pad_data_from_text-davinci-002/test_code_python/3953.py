def solution():
    percent_of_total = 20
    total_goals = 300
    goals_scored = total_goals * (percent_of_total/100)
    player_1_goals = goals_scored / 2
    player_2_goals = player_1_goals
    return player_1_goals, player_2_goals

print(solution())