def solution():
    """Juanico is 4 years less than half the age of Gladys. If Gladys will be 40 years old ten years from now, calculate Juanico's age 30 years from now."""
    # Calculate Gladys' age now
    gladys_age_now = 40 - 10
    # Calculate Juanico's age now
    juanico_age_now = gladys_age_now / 2 - 4
    # Calculate Juanico's age 30 years from now
    juanico_age_30_years = juanico_age_now + 30
    result = juanico_age_30_years
    return result

print(solution())