def solution():
    initial_count = 4  # There are initially 4 alligators
    doubling_time = 6  # The number of alligators doubles every 6 months
    time_in_years = 1  # We want to know the number of alligators after 1 year

    # Calculate the number of doubling periods in 1 year
    doubling_periods = time_in_years * 12 / doubling_time

    # Calculate the final number of alligators
    final_count = initial_count * 2 ** doubling_periods
    result = final_count
    return result

print(solution())