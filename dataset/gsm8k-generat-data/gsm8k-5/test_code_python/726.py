def solution():
    jed_age_in_10_years = 25  # Jed will be 25 years old in 10 years
    jed_age_now = jed_age_in_10_years - 10  # Jed's current age can be found by subtracting 10 from his age in 10 years
    matt_age_now = jed_age_now - 10  # Matt's age is 10 years less than Jed's age
    sum_of_ages = jed_age_now + matt_age_now  # Calculate the sum of their present ages
    result = sum_of_ages
    return result

print(solution())