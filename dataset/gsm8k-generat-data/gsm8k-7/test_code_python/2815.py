def solution():
    current_age_nora = 10
    years_ahead = 10
    ratio_age_terry_nora = 4

    # Calculate Terry's age in 10 years
    age_terry_10_years = ratio_age_terry_nora * current_age_nora

    # Calculate Terry's current age by subtracting 10 years
    current_age_terry = age_terry_10_years - years_ahead
    result = current_age_terry
    return result

print(solution())