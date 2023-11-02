def solution():
    """The minimum age required to be employed at a company is 25 years. Dara aspires to work for the company and will be half the age of Jane in six years. If Jane is currently working for the company and is 28 years old, how long is it before Dara reaches the minimum age required by the company to be employed?"""
    # Define the minimum age required to be employed
    MIN_REQUIRED_AGE = 25

    # Get the current age of Jane
    jane_age = 28

    # Calculate Dara's age in six years
    dara_age_in_6_years = jane_age * 0.5 + 6

    # Calculate the number of years until Dara meets the minimum age requirement
    years_until_minimum_age = MIN_REQUIRED_AGE - dara_age_in_6_years

    # Display the number of years until Dara meets the minimum age requirement
    result = years_until_minimum_age
    return result

print(solution())