def solution():
    """Lily types 15 words a minute and takes a 2-minute break every 10 minutes. How long does it take for Lily to type 255 words?"""
    # Define Lily's typing speed and break interval
    typing_speed = 15 # words per minute
    break_interval = 10 # minutes
    break_duration = 2 # minutes

    # Calculate the time it takes for Lily to type the given number of words
    total_typing_time = 255 / typing_speed # minutes

    # Calculate the number of breaks Lily takes during the typing time
    break_count = total_typing_time // break_interval

    # Calculate the total break time
    total_break_time = break_count * break_duration

    # Calculate the total time taken by Lily to type the words
    total_time = total_typing_time + total_break_time

    # return the result
    result = total_time
    return result

print(solution())