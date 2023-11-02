def solution():
    """In five years, Grant will be 2/3 the age of the hospital that he is hired into. If Grant is currently 25 years old, how old is the hospital now?"""
    grant_age_in_5_years = 30
    current_grant_age = 25
    ratio_of_age = 2/3
    hospital_age_in_5_years = grant_age_in_5_years / ratio_of_age
    current_hospital_age = hospital_age_in_5_years - 5
    result = current_hospital_age
    return result

print(solution())