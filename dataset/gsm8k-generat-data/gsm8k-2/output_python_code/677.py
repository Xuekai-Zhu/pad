def solution():
    """Belinda can throw a ball at a speed of 20 feet/second. If the ball flies for 8 seconds before hitting the ground, and Belinda's border collie can run 5 feet/second, how many seconds will it take the border collie to catch up to the ball?"""
    ball_speed = 20
    ball_flight_time = 8
    ball_distance = ball_speed * ball_flight_time
    border_collie_speed = 5
    time_to_catch_up = ball_distance / (ball_speed - border_collie_speed)
    result = time_to_catch_up
    return result

print(solution())