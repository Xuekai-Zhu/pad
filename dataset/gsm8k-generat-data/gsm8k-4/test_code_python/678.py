def solution():
    """Belinda can throw a ball at a speed of 20 feet/second. If the ball flies for 8 seconds before hitting the ground, and Belinda's border collie can run 5 feet/second, how many seconds will it take the border collie to catch up to the ball?"""
    # Define the initial speed of the ball and the time it's in the air
    ball_speed = 20 # feet/second
    ball_time = 8 # seconds

    # Calculate the distance the ball has traveled before hitting the ground
    ball_distance = ball_speed * ball_time # feet

    # Define the speed of the border collie
    collie_speed = 5 # feet/second

    # Calculate how long it takes the collie to catch up to the ball
    collie_time = ball_distance / collie_speed # seconds

    result = collie_time
    return result

print(solution())