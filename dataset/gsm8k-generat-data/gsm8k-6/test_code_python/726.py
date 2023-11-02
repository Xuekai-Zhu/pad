def solution():
    # Find Jed's present age
    jed_age_10_years_later = 25
    jed_present_age = jed_age_10_years_later - 10

    # Find Matt's present age
    matt_present_age = jed_present_age - 10

    # Find the sum of their present ages
    sum_of_ages = jed_present_age + matt_present_age
    result = sum_of_ages
    return result

print(solution())