def solution():
    shampoo_per_use = 1/4  # Brittany uses 1/4 ounce of shampoo every other day
    days_per_leap_year = 366  # There are 366 days in a leap year
    uses_per_year = days_per_leap_year // 2  # Brittany uses shampoo every other day, so she uses it half the number of days in a year
    ounces_per_year = shampoo_per_use * uses_per_year  # Total ounces of shampoo Brittany uses in a year
    bottles_needed = ounces_per_year / 14  # Divide total ounces by ounces per bottle to get number of bottles needed
    result = bottles_needed
    return result

print(solution())