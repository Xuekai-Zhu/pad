def solution():
    
    first_dose_wait = 20
    second_dose_wait = first_dose_wait / 2
    total_wait_time = first_dose_wait + second_dose_wait
    result = total_wait_time
    return result

print(solution())