def solution():
    wait_time_first_dose = 20
    wait_time_second_dose = wait_time_first_dose / 2

    total_wait_time = wait_time_first_dose + wait_time_second_dose
    result = total_wait_time
    return result

print(solution())