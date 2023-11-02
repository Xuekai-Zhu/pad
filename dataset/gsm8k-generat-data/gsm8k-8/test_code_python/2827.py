def solution():
    # Calculate Grant's age in 5 years
    grant_age_5_years = 25 + 5

    # Calculate the hospital's age in 5 years
    hospital_age_5_years = (3/2) * grant_age_5_years

    # Calculate the hospital's current age
    hospital_age_now = hospital_age_5_years - 5
    result = hospital_age_now
    return result

print(solution())