def solution():
    # Define the speeds and head start distance
    dog_speed = 24
    rabbit_speed = 15
    head_start = 0.6

    # Calculate the relative speed between the dog and rabbit
    relative_speed = dog_speed - rabbit_speed

    # Calculate how long it takes the dog to travel the head start distance
    time_to_catch_up = head_start / relative_speed

    # Convert the time to minutes
    time_in_minutes = time_to_catch_up * 60
    result = time_in_minutes
    return result

print(solution())