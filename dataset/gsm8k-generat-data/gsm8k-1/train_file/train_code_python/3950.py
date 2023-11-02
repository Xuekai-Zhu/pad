def solution():
    """Kelsey turned 25 in 1999. Her older sister was born 3 years before Kelsey. It's currently 2021. How old is Kelsey's older sister?"""
    kelsey_age_in_1999 = 25
    kelsey_birth_year = 1999 - kelsey_age_in_1999
    sister_birth_year = kelsey_birth_year - 3
    sister_age_in_2021 = 2021 - sister_birth_year
    result = sister_age_in_2021
    return result

print(solution())