def solution():
    """The minimum age required to be employed at a company is 25 years. Dara aspires to work for the company and will be half the age of Jane in six years. If Jane is currently working for the company and is 28 years old, how long is it before Dara reaches the minimum age required by the company to be employed?"""
    min_age = 25
    jane_age = 28
    dara_age_in_6_years = jane_age / 2
    dara_age_now = dara_age_in_6_years - 6
    years_to_reach_min_age = min_age - dara_age_now
    result = years_to_reach_min_age
    return result

print(solution())