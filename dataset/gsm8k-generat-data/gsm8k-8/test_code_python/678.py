def solution():
    # Calculate the distance the ball travels before hitting the ground
    ball_distance = 20 * 8

    # Calculate the time it takes for the ball to hit the ground
    ball_time = 8

    # Calculate how far the border collie can run in the same amount of time
    collie_distance = 5 * ball_time

    # Calculate how long it will take the collie to catch up to the ball
    collie_time = ball_distance / (20 + 5)

    result = collie_time
    return result

print(solution())