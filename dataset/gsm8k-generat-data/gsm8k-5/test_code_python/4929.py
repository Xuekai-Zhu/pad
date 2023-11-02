def solution():
    # Calculate John's age 3 years ago
    johns_age_3_years_ago = 39 - 3

    # Calculate James' age in 6 years
    james_age_in_6_years = (johns_age_3_years_ago / 2) + 6

    # Calculate James' current age
    james_age = james_age_in_6_years - 6

    # Calculate James' older brother's age
    older_brother_age = james_age + 4

    result = older_brother_age
    return result

print(solution())