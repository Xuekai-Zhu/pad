def solution():
    goals_scored_against_Barca = 300
    percentage_of_goals_scored = 0.2
    total_goals_scored = goals_scored_against_Barca / percentage_of_goals_scored
    
    # The goals scored by the two players is equal, so we divide by 2 to get individual goals
    player_goals = total_goals_scored / 2
    result = player_goals
    return result

print(solution())