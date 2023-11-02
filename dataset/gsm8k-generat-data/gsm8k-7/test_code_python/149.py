def solution():
    ernesto_age = 11
    jayden_age_ratio = 0.5
    time_difference = 3 # in years

    # Calculate Jayden's age in 3 years
    ernesto_age_in_3_years = ernesto_age + time_difference
    jayden_age_in_3_years = 2 * ernesto_age_in_3_years * jayden_age_ratio

    # Calculate Jayden's current age
    jayden_current_age = jayden_age_in_3_years - time_difference
    result = jayden_current_age
    return result

print(solution())