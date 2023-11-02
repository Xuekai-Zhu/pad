def solution():
    # Define James' current age and Janet's current age
    james_age = 37 - 15
    janet_age = james_age / 2

    # Calculate Janet's age 8 years ago
    janet_age_8_years_ago = janet_age - 8

    # Calculate Susan's current age
    susan_age = 3 + janet_age_8_years_ago

    # Calculate Susan's age in 5 years
    susan_age_in_5_years = susan_age + 5

    result = susan_age_in_5_years
    return result

print(solution())