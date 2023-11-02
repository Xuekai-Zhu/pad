def solution():
    # Calculate the total wait time for the swings
    swings_wait_time = 3 * 2  # 3 kids waiting for the swings and each kid waits for 2 minutes

    # Calculate the total wait time for the slide
    slide_wait_time = (2 * 2) * 15  # Twice as many kids waiting for the slide and each kid waits for 15 seconds

    # Calculate the difference in wait times
    shorter_wait_time = slide_wait_time - swings_wait_time

    # Convert the wait time to seconds
    shorter_wait_time_seconds = shorter_wait_time * 60

    result = shorter_wait_time_seconds
    return result

print(solution())