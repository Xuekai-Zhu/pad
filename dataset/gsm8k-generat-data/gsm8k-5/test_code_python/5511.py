def solution():
    nate_age = 14  # Nate is currently 14 years old
    ember_age = nate_age / 2  # Ember is half as old as Nate

    # Calculate the difference in years between Ember's current age and when she will be 14
    age_difference = 14 - ember_age

    # Add the age difference to Nate's current age to find his age when Ember is 14
    nate_age_when_ember_is_14 = nate_age + age_difference
    result = nate_age_when_ember_is_14
    return result

print(solution())