def solution():
    # Define Jackson's current age
    jackson_age = 20

    # Calculate Mandy's current age
    mandy_age = jackson_age + 10

    # Calculate Adele's current age
    adele_age = 0.75 * jackson_age

    # Calculate their total age 10 years from now
    total_age_in_10_years = (jackson_age + 10) + (mandy_age + 10) + (adele_age + 10)
    result = total_age_in_10_years
    return result

print(solution())