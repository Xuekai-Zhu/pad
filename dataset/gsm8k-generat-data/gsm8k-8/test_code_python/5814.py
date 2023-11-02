def solution():
    # Define the total assigned reading time
    total_reading_time = 60

    # Define the time Hillary has already read
    friday_reading_time = 16
    saturday_reading_time = 28
    already_read = friday_reading_time + saturday_reading_time

    # Calculate the time remaining to complete the assignment
    remaining_time = total_reading_time - already_read
    result = remaining_time
    return result

print(solution())