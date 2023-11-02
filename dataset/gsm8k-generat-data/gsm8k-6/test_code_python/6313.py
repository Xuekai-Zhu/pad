def solution():
    brother_age_20_years_ago = 32 - 20  # brother's age 20 years ago
    trevor_age_20_years_ago = brother_age_20_years_ago / 2  # Trevor's age 20 years ago was half of his brother's age
    trevor_age_a_decade_ago = trevor_age_20_years_ago - 10  # Trevor's age 10 years after 20 years ago (30 years ago)
    result = trevor_age_a_decade_ago
    return result

print(solution())