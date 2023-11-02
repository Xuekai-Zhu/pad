def solution():
    num_math_problems = 15
    math_time_per_problem = 2  # minutes per problem

    num_social_studies_problems = 6
    social_studies_time_per_problem = 0.5  # minutes per problem

    num_science_problems = 10
    science_time_per_problem = 1.5  # minutes per problem

    # Calculate the total time Brooke spends on math problems
    math_time = num_math_problems * math_time_per_problem

    # Calculate the total time Brooke spends on social studies problems
    social_studies_time = num_social_studies_problems * social_studies_time_per_problem

    # Calculate the total time Brooke spends on science problems
    science_time = num_science_problems * science_time_per_problem

    # Calculate the total time Brooke spends on all homework
    total_time = math_time + social_studies_time + science_time
    result = total_time
    return result

print(solution())