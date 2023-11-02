def solution():
    """For homework, Brooke has 15 math problems, 6 social studies problems, and 10 science problems. He can answer each math problem for 2 minutes while answering each social studies problem takes him 30 seconds. If he can answer each science problem in 1.5 minutes, how long will it take Brooke to answer all his homework?"""
    math_problems = 15
    social_studies_problems = 6
    science_problems = 10
    time_per_math_problem = 2
    time_per_social_studies_problem = 0.5
    time_per_science_problem = 1.5
    total_time = math_problems * time_per_math_problem + social_studies_problems * time_per_social_studies_problem + science_problems * time_per_science_problem
    result = total_time
    return result

print(solution())