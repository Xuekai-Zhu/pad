def solution():
    
    louie_last_match_goals = 4
    louie_previous_season_goals = 40
    brother_last_match_goals = louie_last_match_goals * 2
    brother_goals_per_season = brother_last_match_goals * 50
    total_brother_goals = brother_goals_per_season * 3
    total_goals = louie_last_match_goals + louie_previous_season_goals + total_brother_goals
    result = total_goals
    return result

print(solution())