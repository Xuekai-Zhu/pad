def solution():
    # Calculate the number of alligators one python can eat in 3 weeks
    alligators_per_week = 1
    python_alligators = alligators_per_week * 3  # one python can eat 3 alligators in 3 weeks

    # Calculate the number of pythons needed to eat 15 alligators in 3 weeks
    pythons_needed = 15 / python_alligators
    result = pythons_needed
    return result

print(solution())