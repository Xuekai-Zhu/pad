def solution():
    """Wade is the star player of the basketball team. His average points per game is 20, and his teammates' average points per game is 40. How many points will their team have in total after 5 games?"""
    # Define Wade's average points per game and his teammates' average points per game
    WADE_POINTS = 20
    TEAM_POINTS = 40

    # Calculate the total points scored by the team in 5 games
    total_points = (WADE_POINTS + TEAM_POINTS) * 5

    # Display the total points
    result = total_points
    return result

print(solution())