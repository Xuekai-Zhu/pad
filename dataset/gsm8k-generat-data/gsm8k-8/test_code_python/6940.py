def solution():
    # Total airing time for 6 programs
    total_time = 6 * 30 * 2 # 6 programs, each with 30 minutes of actual content and commercials

    # Total time spent on commercials for 6 programs
    commercials_time = total_time / 4

    result = commercials_time
    return result

print(solution())