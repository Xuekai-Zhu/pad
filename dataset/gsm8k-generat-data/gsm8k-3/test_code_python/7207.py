def solution():
    """If the first skyscraper was built 100 years ago, how many years in the future will it be 5 years before its 200th anniversary of being built?"""
    # Calculate the number of years from the first skyscraper's construction to its 200th anniversary
    years_to_200th_anniversary = 200 - 100

    # Calculate the number of years until it is 5 years before the 200th anniversary
    years_in_the_future = years_to_200th_anniversary - 5

    # Display the number of years in the future
    result = years_in_the_future
    return result

print(solution())