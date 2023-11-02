def solution():
    """There are 4 alligators living on a golf course in Florida. If the number of alligators doubles every six months, how many alligators will there be at the end of a year?"""
    # Define the initial number of alligators
    initial_alligators = 4

    # Define the number of alligators after 6 months
    first_six_months_alligators = initial_alligators * 2

    # Define the number of alligators after 12 months
    final_alligators = first_six_months_alligators * 2

    # Display the final number of alligators
    result = final_alligators
    return result

print(solution())