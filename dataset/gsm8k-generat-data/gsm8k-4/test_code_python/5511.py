def solution():
    """Ember is half as old as Nate who is 14. When she is 14 herself, how old will Nate be?"""
    # Define Nate's age
    nate_age = 14

    # Calculate Ember's current age
    ember_age = nate_age / 2

    # Calculate the number of years until Ember is 14
    years_to_ember_14 = 14 - ember_age

    # Calculate Nate's age when Ember is 14
    nate_age_at_ember_14 = nate_age + years_to_ember_14

    # Return the result
    result = nate_age_at_ember_14
    return result

print(solution())