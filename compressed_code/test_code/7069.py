def solution():
    
    pairs_per_hour = 3
    work_hours_mon_thurs = 4 * 8
    work_hours_fri = 3
    total_work_hours = work_hours_mon_thurs + work_hours_fri
    total_pairs = total_work_hours * pairs_per_hour
    result = total_pairs
    return result

print(solution())