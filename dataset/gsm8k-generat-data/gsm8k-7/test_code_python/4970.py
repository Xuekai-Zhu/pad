def solution():
    mother_age_now = 41
    years_ago = 5

    # Calculate the mother's age 5 years ago
    mother_age_5_years_ago = mother_age_now - years_ago

    # Calculate the daughter's age 5 years ago
    daughter_age_5_years_ago = mother_age_5_years_ago / 2

    # Calculate the daughter's current age
    daughter_age_now = daughter_age_5_years_ago + years_ago

    # Calculate the daughter's age in 3 years
    daughter_age_in_3_years = daughter_age_now + 3
    result = daughter_age_in_3_years
    return result

print(solution())