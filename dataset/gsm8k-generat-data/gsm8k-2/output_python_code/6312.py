def solution():
    """Trevor's older brother was twice his age 20 years ago. How old was Trevor a decade ago if his brother is now 32 years old?"""
    brother_age_20_years_ago = 32 - 20
    brother_age_10_years_ago = brother_age_20_years_ago + 10
    trevor_age_20_years_ago = brother_age_20_years_ago / 2
    trevor_age_10_years_ago = trevor_age_20_years_ago + 10
    result = trevor_age_10_years_ago
    return result

print(solution())