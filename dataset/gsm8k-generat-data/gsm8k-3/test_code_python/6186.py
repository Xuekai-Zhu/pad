def solution():
    """Tom turned 32 years old 5 years ago.  7 years ago Jim was 5 years older than half Tom's age.  How old is Jim in 2 years?"""
    # Calculate Tom's current age
    tom_age = 32 + 5

    # Calculate Tom's age 7 years ago
    tom_age_7_yrs_ago = tom_age - 7

    # Calculate half of Tom's age 7 years ago
    half_tom_age_7_yrs_ago = tom_age_7_yrs_ago / 2

    # Calculate Jim's age 7 years ago
    jim_age_7_yrs_ago = half_tom_age_7_yrs_ago + 5

    # Calculate Jim's current age
    jim_age = jim_age_7_yrs_ago + 7

    # Calculate Jim's age in 2 years
    jim_age_in_2_yrs = jim_age + 2

    # Display Jim's age in 2 years
    result = jim_age_in_2_yrs
    return result

print(solution())