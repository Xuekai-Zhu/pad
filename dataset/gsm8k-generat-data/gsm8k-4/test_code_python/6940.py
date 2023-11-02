def solution():
    """One-fourth of the airing time of a television program is spent on commercials. If there are 6 thirty-minute programs, how many minutes are spent on commercials for the whole duration of the 6 programs?"""
    # Define the number of programs and the duration of each program in minutes
    num_programs = 6
    program_duration = 30

    # Calculate the total duration of all programs in minutes
    total_duration = num_programs * program_duration

    # Calculate the duration of commercials in minutes
    commercial_duration = total_duration / 4

    # Return the result
    result = commercial_duration
    return result

print(solution())