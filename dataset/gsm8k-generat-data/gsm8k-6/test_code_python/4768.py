def solution():
    # Calculate the total wait time for both doses
    first_dose_wait_time = 20
    second_dose_wait_time = first_dose_wait_time / 2
    total_wait_time = first_dose_wait_time + second_dose_wait_time
    result = total_wait_time
    return result

print(solution())