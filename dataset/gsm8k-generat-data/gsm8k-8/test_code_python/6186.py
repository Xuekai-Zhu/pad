def solution():
    # Calculate Tom's current age
    tom_current_age = 32 + 5

    # Calculate Jim's age 7 years ago
    jim_age_7_years_ago = tom_current_age / 2 + 5

    # Calculate Jim's current age
    jim_current_age = jim_age_7_years_ago + 7

    # Calculate Jim's age in 2 years
    jim_age_in_2_years = jim_current_age + 2

    result = jim_age_in_2_years
    return result

print(solution())