def solution():
    """If the first skyscraper was built 100 years ago, how many years in the future will it be 5 years before its 200th anniversary of being built?"""
    years_since_building = 100
    years_until_200th_anniversary = 200 - years_since_building
    years_before_200th_anniversary = years_until_200th_anniversary - 5
    result = years_before_200th_anniversary
    return result

print(solution())