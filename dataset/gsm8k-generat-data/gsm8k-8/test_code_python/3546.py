def solution():
    # Calculate the total number of alligators that need to be eaten
    total_alligators = 15

    # Calculate the number of alligators that can be eaten in 3 weeks by 1 python
    alligators_per_week = 1 * 3

    # Calculate the number of pythons needed to eat all the alligators
    pythons_needed = total_alligators / alligators_per_week

    result = pythons_needed
    return result

print(solution())