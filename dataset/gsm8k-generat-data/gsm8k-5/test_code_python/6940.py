def solution():
    program_duration = 30  # Each program is 30 minutes long
    commercial_ratio = 1 / 4  # One-fourth of the airing time is spent on commercials
    num_programs = 6  # There are 6 programs in total

    # Calculate the total number of minutes spent on commercials during the 6 programs
    total_commercial_minutes = program_duration * commercial_ratio * num_programs

    result = total_commercial_minutes
    return result

print(solution())