def solution():
    """It takes 3 men an hour to complete a job. If they are hired to work on 5 such similar jobs by a company that pays each of them $10 per hour, calculate the total amount of money the three will earn when they complete the jobs?"""
    num_men = 3
    job_time = 1
    num_jobs = 5
    pay_rate = 10
    total_time = num_men * job_time * num_jobs
    total_pay = total_time * pay_rate
    result = total_pay
    return result

print(solution())