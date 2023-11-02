def solution():
    # Calculate Tom's current age
    tom_age = 32 + 5  # Tom turned 32 five years ago

    # Calculate Jim's age 7 years ago
    jim_age_7_years_ago = (tom_age / 2) + 5  # Jim was 5 years older than half Tom's age

    # Calculate Jim's current age
    jim_age = jim_age_7_years_ago + 7  # Add 7 years to Jim's age 7 years ago

    # Calculate Jim's age in 2 years
    jim_age_in_2_years = jim_age + 2

    result = jim_age_in_2_years
    return result

print(solution())