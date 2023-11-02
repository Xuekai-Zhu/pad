def solution():
    """One-fourth of the airing time of a television program is spent on commercials. If there are 6 thirty-minute programs, how many minutes are spent on commercials for the whole duration of the 6 programs?"""
    program_length = 30
    total_programs = 6
    commercial_ratio = 1/4
    total_commercial_time = program_length * commercial_ratio * total_programs
    result = total_commercial_time
    return result

print(solution())