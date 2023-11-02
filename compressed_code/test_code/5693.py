def solution():
    
    months_in_year = 12
    total_months = 9 * months_in_year
    miles_per_four_months = 37000
    miles_per_month = miles_per_four_months / 4
    total_miles = total_months * miles_per_month
    result = total_miles
    return result

print(solution())