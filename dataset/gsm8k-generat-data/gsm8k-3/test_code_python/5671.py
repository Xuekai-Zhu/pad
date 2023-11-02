def solution():
    """For homework, Brooke has 15 math problems, 6 social studies problems, and 10 science problems. He can answer each math problem for 2 minutes while answering each social studies problem takes him 30 seconds. If he can answer each science problem in 1.5 minutes, how long will it take Brooke to answer all his homework?"""
    # Define the time in minutes it takes to complete each problem
    math_time = 2
    social_studies_time = 0.5
    science_time = 1.5

    # Define the number of problems in each subject
    math_problems = 15
    social_studies_problems = 6
    science_problems = 10

    # Calculate the total time it will take to complete all the problems
    total_time = (math_time * math_problems) + (social_studies_time * social_studies_problems) + (science_time * science_problems)

    # Display the total time in minutes
    result = total_time
    return result

print(solution())