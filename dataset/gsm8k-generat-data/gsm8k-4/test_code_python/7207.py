def solution():
    """If the first skyscraper was built 100 years ago, how many years in the future will it be 5 years before its 200th anniversary of being built?"""
    # Define the year the first skyscraper was built and the year of its 200th anniversary
    first_year = 100  # years ago
    anniversary_year = first_year + 200

    # Calculate the year that is 5 years before the 200th anniversary
    target_year = anniversary_year - 5

    # Calculate the number of years in the future from the current year
    years_in_future = target_year - first_year

    result = years_in_future
    return result

print(solution())