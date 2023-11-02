def solution():
    louie_last_season_goals = 4
    louie_previous_seasons_goals = 40
    louie_total_goals = louie_last_season_goals + louie_previous_seasons_goals

    brother_goals_per_game = 2 * louie_last_season_goals
    brother_total_goals = brother_goals_per_game * 50 * 3

    total_goals = louie_total_goals + brother_total_goals
    result = total_goals
    return result

print(solution())