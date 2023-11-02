def solution():
    # Calculate the total number of hours needed to complete one job
    one_job_hours = 3

    # Calculate the total number of hours needed to complete all 5 jobs
    all_jobs_hours = one_job_hours * 5

    # Calculate the total amount earned by one man after completing all 5 jobs
    one_man_earnings = all_jobs_hours * 10

    # Calculate the total amount earned by three men after completing all 5 jobs
    three_men_earnings = one_man_earnings * 3

    result = three_men_earnings
    return result

print(solution())