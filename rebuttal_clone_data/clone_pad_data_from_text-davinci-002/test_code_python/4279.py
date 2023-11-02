def solution():
    naps_per_day = 6
    nap_duration = 7
    work_duration = 24 - nap_duration
    total_work_hours = naps_per_day * work_duration
    result = total_work_hours
    return result

print(solution())