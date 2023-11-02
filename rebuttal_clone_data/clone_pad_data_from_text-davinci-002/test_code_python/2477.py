def solution():
    total_wages = 160
    hours_worked_2nd_job = 12
    hourly_rate_2nd_job = 9
    wages_2nd_job = hours_worked_2nd_job * hourly_rate_2nd_job
    wages_1st_job = total_wages - wages_2nd_job
    result = wages_1st_job
    return result

print(solution())