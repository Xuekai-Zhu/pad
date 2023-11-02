def solution():
    # Calculate how many years have passed since the first skyscraper was built
    years_passed = 100

    # Calculate how many years until the 200th anniversary
    years_to_200th_anniversary = 200 - years_passed

    # Subtract 5 years from the years to the 200th anniversary to get the future year
    future_year = years_to_200th_anniversary - 5
    result = future_year
    return result

print(solution())