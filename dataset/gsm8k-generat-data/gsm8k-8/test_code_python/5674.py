def solution():
    # Calculate the length of the python after it swallowed the first alligator
    python_length = 1.4 + 0.5

    # Calculate the number of weeks in 616 days
    num_weeks = 616 / 7

    # Calculate the maximum number of alligators the python can eat
    max_num_alligators = int((python_length * 100) / 50 * num_weeks)

    result = max_num_alligators
    return result

print(solution())