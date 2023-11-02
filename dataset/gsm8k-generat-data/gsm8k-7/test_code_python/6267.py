def solution():
    total_minutes_in_day = 24*60
    tv_time = total_minutes_in_day * (1/5)
    remaining_time = total_minutes_in_day - tv_time
    study_time = remaining_time * (1/4)
    result = study_time
    return result

print(solution())