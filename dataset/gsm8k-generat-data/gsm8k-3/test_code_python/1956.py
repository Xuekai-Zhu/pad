def solution():
    """It takes Matt 2 minutes per problem to do his math homework with a calculator and 5 minutes per problem without a calculator. If Matt's assignment has 20 problems, how much time will using a calculator save?"""
    # Define the time saved per problem when using a calculator
    TIME_SAVED = 3

    # Define the number of problems in the assignment
    num_problems = 20

    # Calculate the time it takes to do the assignment with a calculator
    with_calculator = num_problems * 2

    # Calculate the time it takes to do the assignment without a calculator
    without_calculator = num_problems * 5

    # Calculate the time saved by using a calculator
    time_saved = without_calculator - with_calculator

    # Display the time saved
    result = time_saved
    return result

print(solution())