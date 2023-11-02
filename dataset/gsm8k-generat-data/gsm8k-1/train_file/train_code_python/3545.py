def solution():
    """If one Burmese python can eat one 50-cm alligator per week, how many Burmese pythons would it take to eat fifteen 50-centimeter alligators in three weeks?"""
    alligators_per_week = 1
    alligators_per_python = alligators_per_week * 3
    weeks = 3
    total_alligators = 15
    pythons_needed = total_alligators / (alligators_per_python * weeks)
    result = pythons_needed
    
    return result

print(solution())