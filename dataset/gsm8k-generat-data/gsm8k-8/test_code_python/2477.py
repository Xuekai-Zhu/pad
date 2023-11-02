def solution():
    # Define variables
    total_wages = 160
    hours_second_job = 12
    rate_second_job = 9

    # Calculate wages from second job
    wages_second_job = hours_second_job * rate_second_job

    # Calculate wages from first job
    wages_first_job = total_wages - wages_second_job
    result = wages_first_job
    return result

print(solution())