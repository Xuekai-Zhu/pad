def solution():
    # Calculate the age of the fourth dig site in years
    fourth_site_age = 8400
    fourth_site_age_years = 2022 - fourth_site_age

    # Calculate the age of the third dig site in years
    third_site_age_years = fourth_site_age_years / 2

    # Calculate the age of the first dig site in years
    first_site_age_years = third_site_age_years - 3700

    # Calculate the age of the second dig site in years
    second_site_age_years = first_site_age_years - 352

    # Convert the age of the second site to AD/BC notation
    second_site_date = -(second_site_age_years - 2022)

    result = second_site_date
    return result

print(solution())