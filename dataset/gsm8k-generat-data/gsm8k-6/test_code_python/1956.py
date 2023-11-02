def solution():
    # Calculate the total time Matt would take with a calculator and without a calculator
    time_with_calculator = 2 * 20  # 2 minutes per problem with a calculator for 20 problems
    time_without_calculator = 5 * 20  # 5 minutes per problem without a calculator for 20 problems

    # Calculate the time saved by using a calculator
    time_saved = time_without_calculator - time_with_calculator
    result = time_saved
    return result

print(solution())