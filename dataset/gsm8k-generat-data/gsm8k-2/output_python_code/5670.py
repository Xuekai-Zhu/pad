def solution():
    """For homework, Brooke has 15 math problems, 6 social studies problems, and 10 science problems.
    He can answer each math problem for 2 minutes while answering each social studies problem takes him 30 seconds.
    If he can answer each science problem in 1.5 minutes, how long will it take Brooke to answer all his homework?"""
    math_problems = 15
    social_studies_problems = 6
    science_problems = 10
    
    math_time = math_problems * 2
    social_studies_time = social_studies_problems * 0.5
    science_time = science_problems * 1.5
    
    total_time = math_time + social_studies_time + science_time
    
    result = total_time
    return result

print(solution())