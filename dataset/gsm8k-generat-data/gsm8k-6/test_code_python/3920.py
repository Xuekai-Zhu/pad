def solution():
    # Calculate the number of alligators after 1 year
    num_alligators = 4 * (2**(12/6))  # the number of alligators will double every 6 months for 1 year (12 months)
    result = num_alligators
    return result

print(solution())