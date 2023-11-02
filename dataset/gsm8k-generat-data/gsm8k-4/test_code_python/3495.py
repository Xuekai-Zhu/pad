def solution():
    """In his first season at Best Hockey's team, Louie scored four goals in the last hockey match of this season. His brother has scored twice as many goals as Louie scored in the last match in each game he's played in each of the three seasons he's been on the team. Each season has 50 games. What is the total number of goals the brothers have scored between them if, in the previous matches, Louie scored 40 goals?"""
    # Define the number of games per season and the number of previous matches Louie scored in
    GAMES_PER_SEASON = 50
    LOUIE_PREVIOUS_GOALS = 40

    # Calculate the number of goals Louie's brother scores in each game
    BROTHER_GOALS_PER_GAME = 2 * 4

    # Calculate the number of games Louie's brother played in each season and the total number of seasons
    BROTHER_GAMES_PER_SEASON = GAMES_PER_SEASON
    TOTAL_SEASONS = 3

    # Calculate the total number of goals Louie's brother scores in all seasons
    brother_total_goals = BROTHER_GOALS_PER_GAME * BROTHER_GAMES_PER_SEASON * TOTAL_SEASONS

    # Calculate the total number of goals Louie and his brother scored together
    total_goals = LOUIE_PREVIOUS_GOALS + 4 + brother_total_goals

    # Return the result
    result = total_goals
    return result

print(solution())