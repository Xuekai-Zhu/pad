def solution():
    total_time_in_day = 24 * 60  # total time in minutes
    tv_time = total_time_in_day / 5  # 1/5 of the day for TV
    remaining_time = total_time_in_day - tv_time  # time left after watching TV
    study_time = remaining_time / 4  # 1/4 of remaining time for studying
    result = study_time
    return result

print(solution())