def solution():
    """Audrey was asleep for 10 hours last night and dreamed for 2/5 of the time. How much of the night was she not dreaming?"""
    # Define the total time Audrey was sleeping
    total_sleep_time = 10

    # Calculate the time Audrey spent dreaming
    dream_time = total_sleep_time * 2/5

    # Calculate the time Audrey spent not dreaming
    not_dream_time = total_sleep_time - dream_time

    # return the result
    result = not_dream_time
    return result

print(solution())