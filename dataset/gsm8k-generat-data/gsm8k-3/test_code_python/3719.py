def solution():
    """Georgia is working on a math test with 75 problems on it. After 20 minutes she has completed 10 problems. After another 20 minutes, she has completed twice as many problems. She has 40 minutes to complete the rest of the test. How many problems does she have left to solve?"""
    # Define the total number of problems on the test
    total_problems = 75

    # Define the time Georgia takes to complete the first 10 problems
    time_1 = 20

    # Define the number of problems Georgia completes in the first 20 minutes
    problems_1 = 10

    # Define the time Georgia takes to complete the first 20 problems
    time_2 = 40

    # Define the number of problems Georgia completes in the first 40 minutes
    problems_2 = problems_1 + (time_2 - time_1) / 20 * (problems_1 * 2 - problems_1)

    # Define the time Georgia has left to complete the remaining problems
    time_left = 40

    # Calculate the number of problems Georgia has left to solve
    problems_left = total_problems - problems_2 - (time_left / 20) * (problems_1 * 2)

    # Display the number of problems Georgia has left to solve
    result = problems_left
    return result

print(solution())