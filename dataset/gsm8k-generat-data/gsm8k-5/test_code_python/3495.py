def solution():
    louie_last_match_goals = 4
    louie_previous_seasons_goals = 40
    brother_goals_per_game = 2 * louie_last_match_goals
    total_brother_goals = brother_goals_per_game * 50 * 3
    total_goals = louie_last_match_goals + louie_previous_seasons_goals + total_brother_goals
    result = total_goals
    return result

print(solution())