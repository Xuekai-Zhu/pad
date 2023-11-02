def solution():
    # Calculate the number of years until the 200th anniversary
    years_to_anniversary = 200 - 100  # anniversary is 100 years from when the skyscraper was built

    # Calculate the number of years until 5 years before the anniversary
    years_before_anniversary = years_to_anniversary - 5

    result = years_before_anniversary
    return result

print(solution())