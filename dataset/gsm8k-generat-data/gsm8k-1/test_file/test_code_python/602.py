def solution():
    """Every 2 miles a car drives the tires rotate 725 times. Jeremy drives 400 miles a month. If each tire can undergo 10,440,000 rotations how many years before the tire needs to be replaced?"""
    miles_per_rotation = 2
    rotations_per_mile = 725
    miles_per_month = 400
    rotations_per_month = miles_per_month * rotations_per_mile
    rotations_per_year = rotations_per_month * 12
    years_until_replace = 10440000 / rotations_per_year
    result = years_until_replace
    return result

print(solution())