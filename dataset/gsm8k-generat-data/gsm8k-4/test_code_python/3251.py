def solution():
    """To keep himself busy in class, Michael makes rubber-band balls. He makes two sizes, large and small. A small ball uses 50 rubber bands. A large ball requires 300 rubber bands. Michael brought a 5,000 pack to class and already made 22 small balls. How many large balls can he make with the remaining rubber bands?"""
    # Define the number of rubber bands in a small ball
    SMALL_BALL_RUBBER_BANDS = 50

    # Define the number of rubber bands in a large ball
    LARGE_BALL_RUBBER_BANDS = 300

    # Define the total number of rubber bands Michael brought to class
    TOTAL_RUBBER_BANDS = 5000

    # Define the number of small balls Michael made
    small_balls_made = 22

    # Calculate the total number of rubber bands used in the small balls
    small_ball_rubber_band_count = small_balls_made * SMALL_BALL_RUBBER_BANDS

    # Calculate the remaining number of rubber bands
    remaining_rubber_bands = TOTAL_RUBBER_BANDS - small_ball_rubber_band_count

    # Calculate the number of large balls Michael can make with the remaining rubber bands
    large_balls_possible = remaining_rubber_bands // LARGE_BALL_RUBBER_BANDS

    result = large_balls_possible
    return result

print(solution())