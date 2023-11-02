def solution():
    dog_speed = 24
    rabbit_speed = 15
    rabbit_head_start = 0.6

    # Calculate the relative speed of the dog to the rabbit
    relative_speed = dog_speed - rabbit_speed

    # Calculate the time it takes for the dog to cover the distance of the rabbit's head start
    time_to_catch_up = rabbit_head_start / relative_speed

    # Convert the time to minutes
    time_in_minutes = time_to_catch_up * 60
    result = time_in_minutes
    return result

print(solution())