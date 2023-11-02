def solution():
    # Calculate Christina's age in 5 years
    christina_age_in_5_years = 40

    # Calculate Christina's current age
    christina_current_age = christina_age_in_5_years - 5

    # Calculate Oscar's age in 15 years, which will be 3/5 * Christina's current age
    oscar_age_in_15_years = (3/5) * christina_current_age

    # Calculate Oscar's current age by subtracting 15 years from his age in 15 years
    oscar_current_age = oscar_age_in_15_years - 15
    result = oscar_current_age
    return result

print(solution())