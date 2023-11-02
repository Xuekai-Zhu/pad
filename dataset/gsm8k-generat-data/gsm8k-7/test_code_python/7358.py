def solution():
    years_driving = 9
    miles_per_period = 37000
    num_periods_per_year = 3

    # Calculate the total number of periods (4-month intervals) Jack has been driving for
    total_periods = years_driving * num_periods_per_year

    # Calculate the total number of miles Jack has driven
    total_miles = total_periods * miles_per_period
    result = total_miles
    return result

print(solution())