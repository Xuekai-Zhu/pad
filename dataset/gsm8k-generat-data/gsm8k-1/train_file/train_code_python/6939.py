def solution():
    """One-fourth of the airing time of a television program is spent on commercials. If there are 6 thirty-minute programs, how many minutes are spent on commercials for the whole duration of the 6 programs?"""
    airing_time = 30
    num_programs = 6
    commercial_percentage = 1/4
    commercial_time = airing_time * commercial_percentage
    total_commercial_time = commercial_time * num_programs
    total_time = airing_time * num_programs
    non_commercial_time = total_time - total_commercial_time
    result = total_commercial_time
    
    return result

print(solution())