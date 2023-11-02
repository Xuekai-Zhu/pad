def solution():
    """Georgia is working on a math test with 75 problems on it. After 20 minutes she has completed 10 problems. After another 20 minutes, she has completed twice as many problems. She has 40 minutes to complete the rest of the test. How many problems does she have left to solve?"""
    # Define the total number of problems on the test
    total_problems = 75

    # Define the number of problems Georgia has already completed
    completed_problems = 10 + 2*(20/20)

    # Define the remaining time Georgia has to complete the test
    remaining_time = 40

    # Calculate the number of problems Georgia needs to complete per minute to finish the test in time
    problems_per_minute = (total_problems - completed_problems) / remaining_time

    # Calculate the number of problems Georgia has left to solve
    problems_left = total_problems - completed_problems - (problems_per_minute * 20)

    # Return the result
    result = problems_left
    return result

print(solution())