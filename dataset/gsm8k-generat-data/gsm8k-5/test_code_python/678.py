def solution():
    ball_speed = 20  # Belinda throws the ball at a speed of 20 feet/second
    ball_flight_time = 8  # The ball flies for 8 seconds before hitting the ground
    ball_distance = ball_speed * ball_flight_time  # The total distance the ball travels before hitting the ground

    collie_speed = 5  # The border collie can run at a speed of 5 feet/second
    collie_distance = 0  # The initial distance between the collie and the ball is 0
    time_elapsed = 0  # Keep track of how much time has elapsed

    while collie_distance < ball_distance:
        collie_distance += collie_speed  # Update the distance the collie has traveled
        time_elapsed += 1  # Increment the time elapsed

    result = time_elapsed
    return result

print(solution())