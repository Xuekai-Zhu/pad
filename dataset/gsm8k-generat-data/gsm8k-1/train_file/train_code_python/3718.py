def solution():
    """Georgia is working on a math test with 75 problems on it. After 20 minutes she has completed 10 problems.
    After another 20 minutes, she has completed twice as many problems. She has 40 minutes to complete the rest of the test.
    How many problems does she have left to solve?"""
    
    total_problems = 75
    time_to_complete_first_10_problems = 20
    problems_completed_in_first_20_min = 10
    time_to_complete_next_set_of_problems = 20
    problems_completed_in_next_20_min = problems_completed_in_first_20_min * 2
    time_remaining = 40
    total_time_spent = time_to_complete_first_10_problems + time_to_complete_next_set_of_problems
    problems_completed = problems_completed_in_first_20_min + problems_completed_in_next_20_min
    average_time_per_problem = total_time_spent / problems_completed
    problems_left_to_solve = total_problems - problems_completed - (time_remaining / average_time_per_problem)
    result = problems_left_to_solve
    return result

print(solution())