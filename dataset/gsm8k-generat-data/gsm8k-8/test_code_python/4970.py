def solution():
    # Calculate the mother's age 5 years ago
    mother_age_5_years_ago = 41 - 5

    # Calculate the daughter's age 5 years ago
    daughter_age_5_years_ago = mother_age_5_years_ago / 2

    # Calculate the daughter's current age
    daughter_current_age = daughter_age_5_years_ago + 5

    # Calculate the daughter's age in 3 years
    daughter_age_in_3_years = daughter_current_age + 3
    result = daughter_age_in_3_years
    return result

print(solution())