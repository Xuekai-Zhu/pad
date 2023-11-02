def solution():
    total_reading_time = 60  # The assignment requires 1 hour of reading
    time_read_so_far = 16 + 28  # Hillary has already read for 16 minutes on Friday and 28 minutes on Saturday

    # Calculate the remaining reading time needed to complete the assignment
    time_remaining = total_reading_time - time_read_so_far
    result = time_remaining
    return result

print(solution())