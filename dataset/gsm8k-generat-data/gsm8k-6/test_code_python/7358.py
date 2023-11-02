def solution():
    # Calculate the total number of miles that Jack has driven in 9 years
    miles_per_year = 37000 * 3  # Jack drives 37000 miles every 4 months, so he drives 111000 miles per year
    total_miles = miles_per_year * 9  # Jack has been driving for 9 years
    result = total_miles
    return result

print(solution())