def solution():
    louie_last_match_goals = 4
    louie_previous_goals = 40

    brother_seasons = 3
    brother_previous_goals = 0
    brother_goal_ratio = 2  # brother's goals per Louie's last match goals
    games_per_season = 50

    # Calculate the brother's total goals in previous seasons
    for i in range(brother_seasons):
        brother_previous_goals += brother_goal_ratio * games_per_season

    # Calculate the total number of goals scored between the two brothers
    total_goals = louie_last_match_goals + louie_previous_goals + brother_previous_goals
    result = total_goals
    return result

print(solution())