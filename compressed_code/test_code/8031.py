def solution():
    
    grant_age_in_5_years = 30
    current_grant_age = 25
    ratio_of_age = 2/3
    hospital_age_in_5_years = grant_age_in_5_years / ratio_of_age
    current_hospital_age = hospital_age_in_5_years - 5
    result = current_hospital_age
    return result

print(solution())