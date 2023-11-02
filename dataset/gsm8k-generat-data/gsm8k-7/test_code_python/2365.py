def solution():
    fourth_dig_site_year = -8400

    # Calculate the year of the third dig site
    third_dig_site_year = fourth_dig_site_year / 2 - 3700

    # Calculate the year of the first dig site
    first_dig_site_year = third_dig_site_year + 3700

    # Calculate the year of the second dig site
    second_dig_site_year = first_dig_site_year - 352

    result = second_dig_site_year
    return result

print(solution())