def solution():
    # Calculate the daughter's age 5 years ago
    daughter_age_5_years_ago = (41-5)/3  # mother's age 5 years ago was twice the daughter's age

    # Calculate the daughter's current age
    daughter_age = daughter_age_5_years_ago + 5

    # Calculate the daughter's age in 3 years
    daughter_age_in_3_years = daughter_age + 3

    result = daughter_age_in_3_years
    return result

print(solution())