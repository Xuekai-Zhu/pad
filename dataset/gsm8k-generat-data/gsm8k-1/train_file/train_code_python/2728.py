def solution():
    """It takes 3 men an hour to complete a job. If they are hired to work on 5 such similar jobs by a company that pays each of them $10 per hour, 
    calculate the total amount of money the three will earn when they complete the jobs?"""
    jobs_to_complete = 5
    time_per_job = 1  # 1 hour
    men_count = 3
    wage_per_hour = 10
    
    total_time = jobs_to_complete * time_per_job
    total_wage = total_time * men_count * wage_per_hour
    result = total_wage
    return result

print(solution())