def solution():
    # Define the number of problems and the time per problem with and without a calculator
    num_problems = 20
    time_calc = 2
    time_no_calc = 5

    # Calculate the total time to complete the assignment with and without a calculator
    total_time_calc = num_problems * time_calc
    total_time_no_calc = num_problems * time_no_calc

    # Calculate the time saved by using a calculator
    time_saved = total_time_no_calc - total_time_calc
    result = time_saved
    return result

print(solution())