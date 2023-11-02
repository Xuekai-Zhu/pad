def solution():
    belinda_speed = 20  # feet/second
    flight_time = 8  # seconds
    border_collie_speed = 5  # feet/second

    # Calculate the distance the ball travels before hitting the ground
    ball_distance = belinda_speed * flight_time

    # Calculate the time it takes for the border collie to catch up to the ball
    collie_time = ball_distance / border_collie_speed
    result = collie_time
    return result

print(solution())