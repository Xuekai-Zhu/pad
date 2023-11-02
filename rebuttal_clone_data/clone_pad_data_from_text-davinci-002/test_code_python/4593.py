def solution():
    ounces_per_day = 1/4
    ounces_per_bottle = 14
    days_in_a_year = 365
    days_in_a_leap_year = 366
    bottles_per_year = days_in_a_year / (ounces_per_day / ounces_per_bottle)
    bottles_per_leap_year = days_in_a_leap_year / (ounces_per_day / ounces_per_bottle)
    difference_in_bottles = bottles_per_leap_year - bottles_per_year
    result = difference_in_bottles
    return result

print(solution())