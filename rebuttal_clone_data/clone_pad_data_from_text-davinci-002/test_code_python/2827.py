def solution():
    grant_age = 25
    age_in_five_years = grant_age + 5
    hospital_age_in_five_years = age_in_five_years * (2/3)
    hospital_age_now = hospital_age_in_five_years - 5
    result = hospital_age_now
    
    return result

print(solution())