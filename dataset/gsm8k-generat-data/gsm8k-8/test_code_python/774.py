def solution():
    # Calculate the total cost of the first job
    job1_cost = (3 * 50) + (3 * 30)

    # Calculate the total cost of the second job
    job2_cost = (2 * 50) + (5 * 30)

    # Calculate the total cost of the third job
    job3_cost = (1 * 50) + (2 * 40) + (3 * 30)

    # Find the job that pays the most
    max_job = max(job1_cost, job2_cost, job3_cost)
    result = max_job
    return result

print(solution())