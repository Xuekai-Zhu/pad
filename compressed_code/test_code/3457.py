def solution():
    
    mcq_time = 15
    fib_time = 25
    total_mcq_time = mcq_time * 30
    total_fib_time = fib_time * 30
    total_study_time = (total_mcq_time + total_fib_time) / 60
    result = total_study_time
    return result

print(solution())