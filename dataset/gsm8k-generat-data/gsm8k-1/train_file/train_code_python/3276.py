def solution():
    """The minimum age required to be employed at a company is 25 years. Dara aspires to work for the company and will be half the age of Jane in six years. If Jane is currently working for the company and is 28 years old, how long is it before Dara reaches the minimum age required by the company to be employed?"""
    jane_age_in_six_years = 28 + 6
    dara_age_in_six_years = jane_age_in_six_years / 2
    dara_age_now = dara_age_in_six_years - 6
    years_to_minimum_age = 25 - dara_age_now
    result = years_to_minimum_age
    return result

print(solution())