def solution():
    """Belinda can throw a ball at a speed of 20 feet/second. If the ball flies for 8 seconds before hitting the ground, and Belinda's border collie can run 5 feet/second, how many seconds will it take the border collie to catch up to the ball?"""
    # Define Belinda's throwing speed and the time the ball is in the air
    BELINDA_SPEED = 20
    AIR_TIME = 8

    # Calculate the distance the ball travels before hitting the ground
    ball_distance = BELINDA_SPEED * AIR_TIME

    # Calculate how long it takes the border collie to cover that distance
    collie_time = ball_distance / 5

    # Display the time it takes the border collie to catch up to the ball
    result = collie_time
    return result

print(solution())