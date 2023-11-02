def solution():
    men_per_job = 3
    jobs = 5
    men_total = men_per_job * jobs
    wage_per_hour = 10
    hours_per_job = 1
    job_total_hours = hours_per_job * jobs
    total_wages = wage_per_hour * job_total_hours * men_total
    result = total_wages
    return result

print(solution())