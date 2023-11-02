def solution():
    # Calculate the number of goals Louie's brother scored in each game of each season
    brother_goals_per_game = 4 * 2  # Louie's brother scored twice as many goals as Louie in the last match
    brother_total_goals = 3 * 50 * brother_goals_per_game  # brother played in 3 seasons, each with 50 games per season

    # Calculate the total number of goals the brothers scored together
    total_goals = brother_total_goals + 40  # add Louie's previous goals to the total

    result = total_goals
    return result

print(solution())