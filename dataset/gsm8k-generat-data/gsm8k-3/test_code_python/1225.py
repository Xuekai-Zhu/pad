def solution():
    """Donovan Mitchell is currently averaging 26 points per game. His team has played 15 games this season. He has a goal of averaging 30 points per game for the entire 20 game season. How many points does he need to average per game to reach his goal?"""
    # Define Donovan Mitchell's current points per game and the number of games played
    CURRENT_POINTS_PER_GAME = 26
    GAMES_PLAYED = 15

    # Define Donovan Mitchell's goal points per game and the total number of games in the season
    GOAL_POINTS_PER_GAME = 30
    TOTAL_GAMES = 20

    # Calculate the total number of points Donovan Mitchell needs to score for the season
    total_points_needed = GOAL_POINTS_PER_GAME * TOTAL_GAMES

    # Calculate the total number of points Donovan Mitchell has scored so far
    total_points_scored = CURRENT_POINTS_PER_GAME * GAMES_PLAYED

    # Calculate the number of points Donovan Mitchell needs to average per game for the rest of the season to reach his goal
    points_needed_per_game = (total_points_needed - total_points_scored) / (TOTAL_GAMES - GAMES_PLAYED)

    # Display the number of points Donovan Mitchell needs to average per game
    result = points_needed_per_game
    return result

print(solution())