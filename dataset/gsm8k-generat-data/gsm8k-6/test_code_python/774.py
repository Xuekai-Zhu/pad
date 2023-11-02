def solution():
    # Calculate the total earnings for each job
    job1_earnings = (3*50) + (3*30)
    job2_earnings = (2*50) + (5*30)
    job3_earnings = (1*50) + (2*40) + (3*30)

    # Find which job earns the most
    max_earnings = max(job1_earnings, job2_earnings, job3_earnings)

    result = max_earnings
    return result

print(solution())