def solution():
    justin_age = 26
    jessica_age_diff = 6
    james_age_diff = jessica_age_diff + 7

    # Calculate Jessica's current age
    jessica_age = justin_age - jessica_age_diff

    # Calculate James' current age
    james_age = jessica_age + james_age_diff

    # Calculate James' age after 5 years
    james_age_after_5_years = james_age + 5
    result = james_age_after_5_years
    return result

print(solution())