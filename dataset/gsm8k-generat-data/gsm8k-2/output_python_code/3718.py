def solution():
    """Georgia is working on a math test with 75 problems on it. After 20 minutes she has completed 10 problems. After another 20 minutes, she has completed twice as many problems. She has 40 minutes to complete the rest of the test. How many problems does she have left to solve?"""
    total_problems = 75
    first_completion_time = 20
    first_completion_problems = 10
    second_completion_time = 40
    second_completion_problems = 2 * first_completion_problems
    remaining_completion_time = 40
    remaining_problems = total_problems - first_completion_problems - second_completion_problems
    result = remaining_problems
    return result

print(solution())