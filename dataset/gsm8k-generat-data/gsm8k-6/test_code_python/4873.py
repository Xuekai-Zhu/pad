def solution():
    # Calculate the relative speed between the dog and the rabbit
    relative_speed = 24 - 15  # the dog is chasing the rabbit

    # Calculate the time it takes for the dog to catch up to the rabbit
    time_to_catch_up = 0.6 / relative_speed  # distance / speed

    # Convert the time to minutes
    time_in_minutes = time_to_catch_up * 60

    result = time_in_minutes
    return result

print(solution())