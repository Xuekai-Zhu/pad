def solution():
    skyscraper_built_year = 1921  # The first skyscraper was built 100 years ago in 1921
    anniversary_year = skyscraper_built_year + 200  # Calculate the year of the 200th anniversary

    # Calculate the year that is 5 years before the 200th anniversary year
    future_year = anniversary_year - 5

    # Calculate the number of years in the future from the current year to the future year
    years_in_future = future_year - 2021
    result = years_in_future
    return result

print(solution())