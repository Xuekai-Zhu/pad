def solution():
    # John's current age
    john_age = 39

    # John's age 3 years ago
    john_age_3_years_ago = john_age - 3

    # James' age in 6 years
    james_age_in_6_years = (john_age_3_years_ago * 2) + 6

    # James' current age
    james_age = james_age_in_6_years - 6

    # James' older brother's age
    older_brother_age = james_age + 4

    result = older_brother_age
    return result

print(solution())