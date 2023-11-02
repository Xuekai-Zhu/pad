def solution():
    
    mc_questions = 30
    fib_questions = 30
    mc_time = 15
    fib_time = 25
    total_study_time = (mc_questions * mc_time + fib_questions * fib_time) / 60
    result = total_study_time
    return result

print(solution())