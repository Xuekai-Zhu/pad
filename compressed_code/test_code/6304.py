def solution():
    
    belinda_speed = 20
    ball_flight_time = 8
    ball_distance = belinda_speed * ball_flight_time
    dog_speed = 5
    time_to_catch = ball_distance / dog_speed
    result = time_to_catch
    return result

print(solution())