def solution():
    """To keep himself busy in class, Michael makes rubber-band balls. He makes two sizes, large and small. A small ball uses 50 rubber bands. A large ball requires 300 rubber bands. Michael brought a 5,000 pack to class and already made 22 small balls. How many large balls can he make with the remaining rubber bands?"""
    # Define the number of rubber bands in a small and large ball
    SMALL_BALL = 50
    LARGE_BALL = 300

    # Define the number of rubber bands in the 5,000 pack after making the small balls
    remaining_bands = 5000 - (22 * SMALL_BALL)

    # Calculate the maximum number of large balls that can be made with the remaining rubber bands
    max_large_balls = remaining_bands // LARGE_BALL

    # Display the maximum number of large balls that can be made
    result = max_large_balls
    return result

print(solution())