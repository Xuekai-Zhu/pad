def solution():
    # Calculate the distance the ball traveled before hitting the ground
    distance_ball = 20 * 8  # Belinda throws the ball at a speed of 20 feet/second for 8 seconds

    # Calculate the time it takes for the border collie to catch up to the ball
    time_to_catch = distance_ball / (20 + 5)  # Belinda's border collie can run at a speed of 5 feet/second faster than the ball
    result = time_to_catch
    return result

print(solution())