def solution():
    typing_speed = 15  # words per minute
    break_time = 2  # minutes
    break_interval = 10  # minutes
    total_words = 255

    # Calculate the total typing time without breaks
    typing_time = total_words / typing_speed

    # Calculate the total number of breaks
    num_breaks = typing_time // break_interval

    # Calculate the total break time
    total_break_time = num_breaks * break_time

    # Calculate the total time to type all words including breaks
    total_time = typing_time + total_break_time
    result = total_time
    return result

print(solution())