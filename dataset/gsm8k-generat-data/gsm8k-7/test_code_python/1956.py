def solution():
    num_problems = 20
    time_per_calculator_problem = 2
    time_per_no_calculator_problem = 5

    # Calculate the total time it would take to do all problems without a calculator
    total_time_no_calculator = num_problems * time_per_no_calculator_problem

    # Calculate the total time it would take to do all problems with a calculator
    total_time_calculator = num_problems * time_per_calculator_problem

    # Calculate the time saved by using a calculator
    time_saved = total_time_no_calculator - total_time_calculator
    result = time_saved
    return result

print(solution())