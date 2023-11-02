def solution():
    
    louie_last_match_goals = 4
    louie_previous_goals = 40
    brother_seasons = 3
    brother_goals_per_game = 2 * louie_last_match_goals
    brother_total_goals = brother_goals_per_game * 50 * brother_seasons
    total_goals = louie_last_match_goals + louie_previous_goals + brother_total_goals
    result = total_goals
    return result

print(solution())