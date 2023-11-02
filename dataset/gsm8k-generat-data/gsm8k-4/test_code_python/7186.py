def solution():
    """During a commercial break in the Super Bowl, there were three 5-minute commercials and eleven 2-minute commercials. How many minutes was the commercial break?"""
    # Define the durations of the commercials
    short_duration = 2
    long_duration = 5

    # Define the number of commercials of each duration
    short_commercials = 11
    long_commercials = 3

    # Calculate the total duration of the commercial break
    total_duration = (short_duration * short_commercials) + (long_duration * long_commercials)

    # return the result
    result = total_duration
    return result

print(solution())