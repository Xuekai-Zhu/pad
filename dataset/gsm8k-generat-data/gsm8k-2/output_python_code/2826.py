def solution():
    """In five years, Grant will be 2/3 the age of the hospital that he is hired into. If Grant is currently 25 years old, how old is the hospital now?"""
    grant_age = 25
    ratio = 2 / 3
    hospital_age_in_5_years = grant_age / ratio
    hospital_age_now = hospital_age_in_5_years - 5
    result = hospital_age_now
    return result

print(solution())