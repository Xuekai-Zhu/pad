def solution():
    """It takes 3 men an hour to complete a job. If they are hired to work on 5 such similar jobs by a company that pays each of them $10 per hour, calculate the total amount of money the three will earn when they complete the jobs?"""
    # Define the number of men and the time to complete a job
    num_men = 3
    time_per_job = 1

    # Define the number of jobs to complete
    num_jobs = 5

    # Define the hourly wage
    hourly_wage = 10

    # Calculate the total time to complete all jobs
    total_time = num_men * time_per_job * num_jobs

    # Calculate the total earnings
    total_earnings = num_men * hourly_wage * total_time

    # Return the result
    result = total_earnings
    return result

print(solution())