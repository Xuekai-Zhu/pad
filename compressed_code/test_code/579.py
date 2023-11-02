def solution():
    
    job1 = (3 * 50) + (3 * 30)
    job2 = (2 * 50) + (5 * 30)
    job3 = (1 * 50) + (2 * 40) + (3 * 30)
    max_money = max(job1, job2, job3)
    result = max_money
    return result

print(solution())