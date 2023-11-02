def solution():
    # Define Nate's current age
    nate_age = 14

    # Calculate Ember's current age
    ember_age = nate_age / 2

    # Calculate how many years until Ember is 14
    years_until_ember_14 = 14 - ember_age

    # Calculate how old Nate will be when Ember is 14
    nate_age_at_ember_14 = nate_age + years_until_ember_14
    result = nate_age_at_ember_14
    return result

print(solution())