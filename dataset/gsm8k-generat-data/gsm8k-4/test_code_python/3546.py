def solution():
    """If one Burmese python can eat one 50-cm alligator per week, how many Burmese pythons would it take to eat fifteen 50-centimeter alligators in three weeks?"""
    # Define the number of alligators and the time needed to eat them
    alligators = 15
    weeks = 3

    # Calculate the number of alligators that can be eaten in three weeks by one python
    alligators_per_python = weeks * 1

    # Calculate the number of pythons needed to eat all the alligators in three weeks
    pythons_needed = alligators / alligators_per_python
    result = math.ceil(pythons_needed)
    return result

print(solution())