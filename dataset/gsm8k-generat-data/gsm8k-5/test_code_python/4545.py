def solution():
    jackson_age = 20  # Jackson is currently 20 years old
    mandy_age = jackson_age + 10  # Mandy is 10 years older than Jackson
    adele_age = (3/4) * jackson_age  # Adele is 3/4 as old as Jackson

    # Calculate their ages 10 years from now
    jackson_age_10_years_later = jackson_age + 10
    mandy_age_10_years_later = mandy_age + 10
    adele_age_10_years_later = adele_age + 10

    # Calculate the total of their ages 10 years from now
    total_age_10_years_later = jackson_age_10_years_later + mandy_age_10_years_later + adele_age_10_years_later
    result = total_age_10_years_later
    return result

print(solution())