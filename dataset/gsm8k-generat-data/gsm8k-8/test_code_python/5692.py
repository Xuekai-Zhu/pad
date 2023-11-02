def solution():
    # Define Sebastian's age and his age 5 years ago
    sebastian_age = 40
    sebastian_age_5_years_ago = sebastian_age - 5

    # Calculate Sebastian's sister's age and her age 5 years ago
    sister_age_5_years_ago = sebastian_age_5_years_ago - 10
    sister_age = sister_age_5_years_ago + 5

    # Calculate their father's age 5 years ago
    sum_ages_5_years_ago = sebastian_age_5_years_ago + sister_age_5_years_ago
    father_age_5_years_ago = (4/3) * sum_ages_5_years_ago

    # Calculate their father's current age
    father_age = father_age_5_years_ago + 5

    result = father_age
    return result

print(solution())