def solution():
    jed_in_10_years = 25
    age_difference = 10

    # Calculate Jed's current age
    jed_current_age = jed_in_10_years - age_difference

    # Calculate Matt's current age
    matt_current_age = jed_current_age - age_difference

    # Calculate the sum of their present ages
    sum_of_ages = jed_current_age + matt_current_age
    result = sum_of_ages
    return result

print(solution())