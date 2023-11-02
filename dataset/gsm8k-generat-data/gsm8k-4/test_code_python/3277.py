def solution():
    """The minimum age required to be employed at a company is 25 years. Dara aspires to work for the company and will be half the age of Jane in six years. If Jane is currently working for the company and is 28 years old, how long is it before Dara reaches the minimum age required by the company to be employed?"""
    # Define the minimum age required to be employed by the company
    MINIMUM_EMPLOYMENT_AGE = 25

    # Define Jane's current age and the time in years until Dara is half her age
    jane_age = 28
    half_age_time = 6

    # Calculate Dara's age in six years when she will be half Jane's age
    dara_half_age = (jane_age + half_age_time) / 2

    # Calculate Dara's current age
    dara_age = dara_half_age - half_age_time

    # Calculate the number of years until Dara reaches the minimum employment age
    years_to_minimum_age = MINIMUM_EMPLOYMENT_AGE - dara_age

    result = years_to_minimum_age
    return result

print(solution())