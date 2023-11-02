def solution():
    """It takes 3 men an hour to complete a job. If they are hired to work on 5 such similar jobs by a company that pays each of them $10 per hour, calculate the total amount of money the three will earn when they complete the jobs?"""
    # Define the number of men and the time it takes to complete one job
    NUM_MEN = 3
    JOB_TIME = 1

    # Define the number of jobs to complete and the pay rate
    NUM_JOBS = 5
    PAY_RATE = 10

    # Calculate the total time it will take to complete all the jobs
    total_time = NUM_MEN * JOB_TIME * NUM_JOBS

    # Calculate the total earnings for all three men
    total_earnings = NUM_MEN * total_time * PAY_RATE

    # Display the total earnings
    result = total_earnings
    return result

print(solution())