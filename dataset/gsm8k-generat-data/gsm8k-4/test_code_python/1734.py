def solution():
    """Wade is the star player of the basketball team. His average points per game is 20, and his teammates' average points per game is 40. How many points will their team have in total after 5 games?"""
    # Define Wade's average points per game and the teammates' average points per game
    wade_points = 20
    teammates_points = 40

    # Calculate the total points for the team in one game
    total_points = wade_points + teammates_points

    # Calculate the total points for the team in 5 games
    total_points_5games = total_points * 5

    # return the result
    result = total_points_5games
    return result

print(solution())