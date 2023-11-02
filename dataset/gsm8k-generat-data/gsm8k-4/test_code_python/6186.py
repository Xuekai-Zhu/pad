def solution():
    """Tom turned 32 years old 5 years ago.  7 years ago Jim was 5 years older than half Tom's age.  How old is Jim in 2 years?"""
    # Calculate Tom's current age
    tom_age = 32 + 5

    # Calculate Jim's age 7 years ago
    jim_age_7 = (tom_age / 2) + 5

    # Determine Jim's current age
    jim_age = jim_age_7 + 7

    # Calculate Jim's age in 2 years
    jim_age_2 = jim_age + 2

    result = jim_age_2
    return result

print(solution())