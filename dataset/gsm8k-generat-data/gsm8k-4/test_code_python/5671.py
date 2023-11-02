def solution():
    """For homework, Brooke has 15 math problems, 6 social studies problems, and 10 science problems. He can answer each math problem for 2 minutes while answering each social studies problem takes him 30 seconds. If he can answer each science problem in 1.5 minutes, how long will it take Brooke to answer all his homework?"""
    # Define the time it takes to answer each type of problem
    math_time = 2 # minutes
    ss_time = 0.5 # minutes
    science_time = 1.5 # minutes

    # Calculate the total time it takes to answer all the math problems
    total_math_time = math_time * 15

    # Calculate the total time it takes to answer all the social studies problems
    total_ss_time = ss_time * 6

    # Calculate the total time it takes to answer all the science problems
    total_science_time = science_time * 10

    # Calculate the total time it takes to answer all the homework problems
    total_time = total_math_time + total_ss_time + total_science_time

    # Return the result in minutes
    result = total_time
    return result

print(solution())