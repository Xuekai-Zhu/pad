def solution():
    # Calculate the distance that Jenny has covered in 0.5 hours
    jenny_distance = 15 * 0.5

    # Start driving the same distance as Jenny
    anna_distance = jenny_distance

    # Calculate the time it takes Anna to catch up to Jenny
    anna_speed = 45
    relative_speed = anna_speed - 15
    time_to_catch_up = anna_distance / relative_speed

    # Convert the time to minutes
    time_in_minutes = time_to_catch_up * 60
    result = time_in_minutes
    return result

print(solution())