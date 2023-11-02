def solution():
    """5 years ago, a mother was twice as old as her daughter. If the mother is 41 years old now, how old will the daughter be in 3 years?"""
    mother_age_now = 41
    daughter_age_5_years_ago = (mother_age_now - 5) / 2
    daughter_age_now = daughter_age_5_years_ago + 5
    daughter_age_in_3_years = daughter_age_now + 3
    result = daughter_age_in_3_years
    return result

print(solution())