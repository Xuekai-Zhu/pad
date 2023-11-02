def solution():
    first_year = 100
    anniversary_year = 200

    # Calculate the number of years from the first skyscraper's construction to its 200th anniversary
    total_years = anniversary_year - first_year

    # Calculate the year that is 5 years before the 200th anniversary
    target_year = first_year + total_years - 5

    # Calculate the number of years in the future from the current year to the target year
    years_in_future = target_year - 2021

    result = years_in_future
    return result

print(solution())