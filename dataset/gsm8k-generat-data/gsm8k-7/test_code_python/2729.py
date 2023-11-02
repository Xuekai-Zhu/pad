def solution():
    num_men = 3
    time_per_job = 1  # in hours
    num_jobs = 5
    pay_rate = 10  # in dollars per hour

    # Calculate the total time it will take for the three men to complete all jobs
    total_time = num_jobs * time_per_job

    # Calculate the total amount of money earned by each man for all jobs
    total_pay_per_man = total_time * pay_rate

    # Calculate the total amount of money earned by all three men for all jobs
    total_earnings = total_pay_per_man * num_men
    result = total_earnings
    return result

print(solution())