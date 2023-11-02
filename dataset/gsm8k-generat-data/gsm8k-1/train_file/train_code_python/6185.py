def solution():
    """Tom turned 32 years old 5 years ago. 7 years ago Jim was 5 years older than half Tom's age. How old is Jim in 2 years?"""
    tom_age_5_years_ago = 32
    tom_age_now = tom_age_5_years_ago + 5
    jim_age_7_years_ago = (tom_age_5_years_ago / 2) + 5
    jim_age_now = jim_age_7_years_ago + 7 + 2
    result = jim_age_now
    return result

print(solution())