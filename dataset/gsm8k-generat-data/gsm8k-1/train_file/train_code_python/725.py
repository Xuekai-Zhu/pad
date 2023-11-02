def solution():
    """Jed is 10 years older than Matt. In 10 years, Jed will be 25 years old. What is the sum of their present ages?"""
    jed_age_in_10_years = 25
    jed_age_now = jed_age_in_10_years - 10
    matt_age_now = jed_age_now - 10
    sum_of_ages = jed_age_now + matt_age_now
    result = sum_of_ages
    return result

print(solution())