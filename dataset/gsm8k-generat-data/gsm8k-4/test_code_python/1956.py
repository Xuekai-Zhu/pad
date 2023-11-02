def solution():
    """It takes Matt 2 minutes per problem to do his math homework with a calculator and 5 minutes per problem without a calculator. If Matt's assignment has 20 problems, how much time will using a calculator save?"""
    # Define the number of problems and the time it takes to do them with and without a calculator
    num_problems = 20
    without_calculator_time = num_problems * 5
    with_calculator_time = num_problems * 2

    # Calculate the time saved by using a calculator
    time_saved = without_calculator_time - with_calculator_time

    # return the result
    result = time_saved
    return result

print(solution())