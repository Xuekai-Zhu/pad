def solution():
    
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