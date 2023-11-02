def solution():
    """Juanico is 4 years less than half the age of Gladys. If Gladys will be 40 years old ten years from now, calculate Juanico's age 30 years from now."""
    # Calculate Gladys' current age
    gladys_age = 30 + 10 - 10  # Gladys will be 40 years old ten years from now

    # Calculate Juanico's current age
    juanico_age = (gladys_age / 2) - 4

    # Calculate Juanico's age 30 years from now
    juanico_age_30_years = juanico_age + 30

    # Display Juanico's age 30 years from now
    result = juanico_age_30_years
    return result

print(solution())