def solution():
    """In his first season at Best Hockey's team, Louie scored four goals in the last hockey match of this season. His brother has scored twice as many goals as Louie scored in the last match in each game he's played in each of the three seasons he's been on the team. Each season has 50 games.  What is the total number of goals the brothers have scored between them if, in the previous matches, Louie scored 40 goals?"""
    # Define Louie's total goals
    louie_goals = 4 + 40

    # Define the number of seasons and games per season
    num_seasons = 3
    games_per_season = 50

    # Calculate the total number of games played by Louie's brother
    total_games = num_seasons * games_per_season

    # Calculate Louie's brother's total goals
    brother_goals = louie_goals * 2 * total_games

    # Calculate the total number of goals scored by the brothers
    total_goals = louie_goals + brother_goals

    # Display the total number of goals
    result = total_goals
    return result

print(solution())