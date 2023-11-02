def solution():
    # Determine their ages 20 years ago
    hannah_age_20_years_ago = 6 - 20
    july_age_20_years_ago = hannah_age_20_years_ago / 2

    # Determine their current ages
    hannah_age = hannah_age_20_years_ago + 20
    july_age = july_age_20_years_ago + 20

    # Determine July's husband's age
    husband_age = july_age + 2

    result = husband_age
    return result

print(solution())