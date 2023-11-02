def solution():
    num_alligators = 4
    num_doublings = 2
    num_months_in_year = 12

    # Calculate the number of doublings in a year
    doublings_in_year = num_months_in_year / 6

    # Calculate the final number of alligators
    final_num_alligators = num_alligators * (num_doublings ** doublings_in_year)
    result = final_num_alligators
    return result

print(solution())