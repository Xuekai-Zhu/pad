def solution():
    dog_speed = 24  # Erik's dog can run 24 miles per hour
    rabbit_speed = 15  # The rabbit can run 15 miles per hour
    head_start = 0.6  # The rabbit has a head start of 0.6 miles

    # Calculate the relative speed of the dog to the rabbit
    relative_speed = dog_speed - rabbit_speed

    # Calculate the time it takes for the dog to catch up to the rabbit
    time_to_catch_up = head_start / relative_speed * 60  # Convert hours to minutes

    result = time_to_catch_up
    return result

print(solution())