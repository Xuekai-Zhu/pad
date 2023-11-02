def solution():
    suzy_age_now = 20
    num_years = 4

    # Calculate Suzy's age in 4 years
    suzy_age_in_4_years = suzy_age_now + num_years

    # Calculate Mary's age in 4 years
    mary_age_in_4_years = suzy_age_in_4_years / 2

    # Calculate Mary's current age
    mary_age_now = mary_age_in_4_years - num_years
    result = mary_age_now
    return result

print(solution())