def solution():
    """Donovan Mitchell is currently averaging 26 points per game. His team has played 15 games this season. He has a goal of averaging 30 points per game for the entire 20 game season. How many points does he need to average per game to reach his goal?"""
    # Define Donovan's current average points per game and the number of games played
    current_average = 26
    games_played = 15

    # Define Donovan's goal average points per game and the total number of games in the season
    goal_average = 30
    total_games = 20

    # Calculate Donovan's total points scored in the season so far
    total_points = current_average * games_played

    # Calculate the total points he needs to score in the remaining games to reach his goal
    remaining_points = (goal_average * total_games) - total_points

    # Calculate the average points he needs to score per game in the remaining games to reach his goal
    average_needed = remaining_points / (total_games - games_played)

    # Return the result
    result = average_needed
    return result

print(solution())