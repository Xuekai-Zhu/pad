def solution():
    jackson_age = 20
    mandy_age = jackson_age + 10
    adele_age = (3/4) * jackson_age

    # Calculate their ages 10 years from now
    jackson_age_10_years = jackson_age + 10
    mandy_age_10_years = mandy_age + 10
    adele_age_10_years = adele_age + 10

    # Calculate the total of their ages 10 years from now
    total_age_10_years = jackson_age_10_years + mandy_age_10_years + adele_age_10_years
    result = total_age_10_years
    return result

print(solution())