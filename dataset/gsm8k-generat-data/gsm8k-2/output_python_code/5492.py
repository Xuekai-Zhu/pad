def solution():
    """Christina's age will be half of 80 years in five years to come. If Oscar will be 3/5 times as old as Christina is now in 15 years, calculate Oscar's age now"""
    christina_age_in_5_years = 80 / 2
    christina_current_age = christina_age_in_5_years - 5
    oscar_age_in_15_years = (3/5) * christina_current_age + 15
    oscar_current_age = oscar_age_in_15_years - 15
    result = oscar_current_age
    return result

print(solution())