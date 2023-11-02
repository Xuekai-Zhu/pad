def solution():
    
    pick_up_time = 5
    vacuum_time = 20
    window_cleaning_time = 15
    dusting_time = 10
    total_time = pick_up_time + vacuum_time + window_cleaning_time + dusting_time
    weeks = 4
    total_time *= weeks
    result = total_time
    return result

print(solution())