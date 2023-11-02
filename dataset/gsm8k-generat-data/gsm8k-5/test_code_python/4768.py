def solution():
    wait_time_first_dose = 20  # John has to wait 20 minutes for the first dose
    wait_time_second_dose = wait_time_first_dose / 2  # The second dose has a wait time half as long
    total_wait_time = wait_time_first_dose + wait_time_second_dose  # Calculate the total wait time

    result = total_wait_time
    return result

print(solution())