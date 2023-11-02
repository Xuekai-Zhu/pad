def solution():
    """John scores 2 shots worth 2 points and 1 shot worth 3 points every 4 minutes. He plays for 2 periods. Each period is 12 minutes. How many points does he score?"""
    # Define the number of shots and points
    SHOTS_2_POINTS = 2
    SHOTS_3_POINTS = 1
    POINTS_2_SHOT = 2
    POINTS_3_SHOT = 3
    MINUTES_PER_PERIOD = 12
    MINUTES_PER_GAME = MINUTES_PER_PERIOD * 2

    # Calculate the number of shots and points per game
    shots_per_game = (MINUTES_PER_GAME / 4) * (SHOTS_2_POINTS + SHOTS_3_POINTS)
    points_per_game = (SHOTS_2_POINTS * POINTS_2_SHOT + SHOTS_3_POINTS * POINTS_3_SHOT) * shots_per_game

    # return the result
    result = points_per_game
    return result

print(solution())