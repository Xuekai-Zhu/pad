def solution():
    """There are 4 alligators living on a golf course in Florida. If the number of alligators doubles every six months, how many alligators will there be at the end of a year?"""
    # Define the initial number of alligators
    initial_alligators = 4

    # Define the number of alligators after 6 months
    six_month_alligators = initial_alligators * 2

    # Define the number of alligators after 1 year (2 sets of 6 months)
    final_alligators = six_month_alligators * 2

    # return the result
    result = final_alligators
    return result

print(solution())