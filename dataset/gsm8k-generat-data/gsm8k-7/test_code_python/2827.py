def solution():
    grant_age = 25
    ratio = 2 / 3  # Grant will be 2/3 the age of the hospital in 5 years

    # Calculate Grant's age in 5 years
    grant_age_5_years = grant_age + 5

    # Calculate the hospital's age in 5 years using the given ratio
    hospital_age_5_years = grant_age_5_years / ratio

    # Calculate the hospital's current age by subtracting 5 years from the age in 5 years
    hospital_age_current = hospital_age_5_years - 5
    result = hospital_age_current
    return result

print(solution())