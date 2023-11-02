def solution():
    brother_age_20_years_ago = 32 - 20  # Trevor's brother was 12 years old 20 years ago
    older_brother_age_a_decade_ago = brother_age_20_years_ago + 10  # Trevor's brother is now 32, so he was 22 a decade ago
    trevor_age_a_decade_ago = older_brother_age_a_decade_ago / 2  # Trevor's brother was twice Trevor's age 20 years ago, so Trevor was half his brother's age
    result = trevor_age_a_decade_ago
    return result

print(solution())