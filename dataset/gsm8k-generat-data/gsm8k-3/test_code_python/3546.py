def solution():
    """If one Burmese python can eat one 50-cm alligator per week, how many Burmese pythons would it take to eat fifteen 50-centimeter alligators in three weeks?"""
    
    # Define the number of alligators one python can eat in a week
    alligators_per_week = 1

    # Define the number of alligators and weeks
    alligators = 15
    weeks = 3

    # Calculate the number of pythons needed to eat all the alligators in 3 weeks
    pythons_needed = alligators / (alligators_per_week * weeks)

    # Round up to the nearest integer
    pythons_needed = math.ceil(pythons_needed)

    # Display the number of pythons needed
    result = pythons_needed
    
    return result

print(solution())