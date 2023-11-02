def solution():
    miles_per_four_months = 37000  # Jack drives 37,000 miles every four months
    months_per_year = 12  # There are 12 months in a year
    total_years = 9  # Jack has been driving for 9 years

    # Calculate the total number of miles Jack has driven in 9 years
    total_miles = miles_per_four_months * (total_years * months_per_year // 4)
    result = total_miles
    return result

print(solution())