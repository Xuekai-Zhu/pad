def solution():
    total_slices = 6 * 12  # Mr. Mitchell bought 6 pizzas, each with 12 slices
    games_played = 8  # The team played 8 games

    # Calculate the total number of goals scored
    total_goals = total_slices / games_played

    # Calculate the average number of goals scored per game
    average_goals = total_goals / games_played
    result = average_goals
    return result

print(solution())