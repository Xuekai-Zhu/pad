def solution():
    current_average = 26  # Donovan Mitchell's current average points per game
    games_played = 15  # His team has played 15 games this season
    total_games = 20  # He wants to average 30 points per game for the entire 20 game season

    # Calculate the total points he needs to score in the remaining 5 games
    remaining_points = (total_games * 30) - (current_average * games_played)

    # Calculate the average points he needs to score in the remaining 5 games
    required_average = remaining_points / (total_games - games_played)
    result = required_average
    return result

print(solution())