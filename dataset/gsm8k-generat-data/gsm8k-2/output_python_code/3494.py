def solution():
    """In his first season at Best Hockey's team, Louie scored four goals in the last hockey match of this season. His brother has scored twice as many goals as Louie scored in the last match in each game he's played in each of the three seasons he's been on the team. Each season has 50 games. What is the total number of goals the brothers have scored between them if, in the previous matches, Louie scored 40 goals?"""
    louie_last_match_goals = 4
    louie_previous_goals = 40
    brother_seasons = 3
    brother_goals_per_game = 2 * louie_last_match_goals
    brother_total_goals = brother_goals_per_game * 50 * brother_seasons
    total_goals = louie_last_match_goals + louie_previous_goals + brother_total_goals
    result = total_goals
    return result

print(solution())