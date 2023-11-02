def solution():
    # Calculate Mandy's age
    mandy_age = 20 + 10  # Mandy is 10 years older than Jackson

    # Calculate Adele's age
    adele_age = (3/4) * 20  # Adele is 3/4 as old as Jackson

    # Calculate their ages 10 years from now
    jackson_in_10_years = 20 + 10
    mandy_in_10_years = mandy_age + 10
    adele_in_10_years = adele_age + 10
    total_age_in_10_years = jackson_in_10_years + mandy_in_10_years + adele_in_10_years
    result = total_age_in_10_years
    return result

print(solution())