def solution():
    num_days = 4
    total_working_hours = num_days * 8 # Assuming an 8-hour workday
    num_naps = 6
    nap_duration = 7

    # Calculate total time spent napping
    total_nap_time = num_naps * nap_duration

    # Calculate total time spent working
    total_working_time = total_working_hours - total_nap_time
    result = total_working_time
    return result

print(solution())