def solution():
    """John decides to get the vaccine for COVID. He has to wait 20 minutes for the first dose. The second dose has a wait time half as long. How long was the total wait time?"""
    first_dose_wait = 20
    second_dose_wait = first_dose_wait / 2
    total_wait_time = first_dose_wait + second_dose_wait
    result = total_wait_time
    return result

print(solution())