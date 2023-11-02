def solution():
    alligators_per_week = 1  # One Burmese python can eat one alligator per week
    alligators_per_3_weeks = 15  # The python needs to eat 15 alligators in 3 weeks

    # Calculate the number of pythons needed to eat the alligators
    pythons_needed = alligators_per_3_weeks / (alligators_per_week * 3)
    result = pythons_needed
    return result

print(solution())