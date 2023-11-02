def solution():
    """Juanico is 4 years less than half the age of Gladys. If Gladys will be 40 years old ten years from now, calculate Juanico's age 30 years from now."""
    gladys_age_now = 30  # Gladys is currently 30 years old
    juanico_age_now = (gladys_age_now / 2) - 4  # Juanico's age now
    juanico_age_30_years = juanico_age_now + 30  # Juanico's age 30 years from now
    result = juanico_age_30_years
    return result

print(solution())