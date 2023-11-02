def solution():
    """Tom turned 32 years old 5 years ago. 7 years ago Jim was 5 years older than half Tom's age. How old is Jim in 2 years?"""
    tom_age_now = 32 + 5
    half_tom_age_7_years_ago = (tom_age_now - 7) / 2
    jim_age_7_years_ago = half_tom_age_7_years_ago + 5
    jim_age_now = jim_age_7_years_ago + 7
    jim_age_in_2_years = jim_age_now + 2
    result = jim_age_in_2_years
    return result

print(solution())