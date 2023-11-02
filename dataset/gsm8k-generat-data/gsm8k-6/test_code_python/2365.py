def solution():
    # Calculate the age of the fourth dig site in years
    fourth_site_age = 2021 - 8400  # convert 8400 BC to AD

    # Calculate the age of the third dig site in years
    third_site_age = fourth_site_age / 2

    # Calculate the age of the first dig site in years
    first_site_age = third_site_age - 3700

    # Calculate the age of the second dig site in years
    second_site_age = first_site_age - 352

    # Calculate the year the archaeologist dated the second dig site
    year_second_site_dated = 2021 - second_site_age

    result = year_second_site_dated
    return result

print(solution())