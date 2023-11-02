def solution():
    """Trevor's older brother was twice his age 20 years ago. How old was Trevor a decade ago if his brother is now 32 years old?"""
    brother_age_20_years_ago = 12
    brother_current_age = 32
    brother_age_difference = brother_current_age - brother_age_20_years_ago
    trevor_age_20_years_ago = brother_age_difference / 2
    trevor_current_age = trevor_age_20_years_ago + 10
    trevor_age_a_decade_ago = trevor_current_age - 10
    result = trevor_age_a_decade_ago
    return result

print(solution())