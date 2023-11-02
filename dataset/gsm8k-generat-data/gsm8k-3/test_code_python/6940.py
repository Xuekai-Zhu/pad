def solution():
    """One-fourth of the airing time of a television program is spent on commercials. If there are 6 thirty-minute programs, how many minutes are spent on commercials for the whole duration of the 6 programs?"""
    # Define the fraction of time spent on commercials
    COMMERCIAL_FRACTION = 1/4

    # Define the duration of each program in minutes
    PROGRAM_DURATION = 30

    # Calculate the total duration of the 6 programs in minutes
    total_duration = 6 * PROGRAM_DURATION

    # Calculate the total duration spent on commercials
    commercial_duration = total_duration * COMMERCIAL_FRACTION

    # Display the duration spent on commercials
    result = commercial_duration
    return result

print(solution())