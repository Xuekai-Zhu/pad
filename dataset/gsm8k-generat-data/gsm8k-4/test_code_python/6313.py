def solution():
    """Trevor's older brother was twice his age 20 years ago. How old was Trevor a decade ago if his brother is now 32 years old?"""
    # Define Trevor's brother's current age and his age 20 years ago
    brother_current_age = 32
    brother_age_20_years_ago = brother_current_age - 20

    # Define Trevor's age 20 years ago
    trevor_age_20_years_ago = brother_age_20_years_ago / 2

    # Define Trevor's current age
    trevor_current_age = trevor_age_20_years_ago + 20

    # Define Trevor's age a decade ago
    trevor_age_a_decade_ago = trevor_current_age - 10

    # return the result
    result = trevor_age_a_decade_ago
    return result

print(solution())