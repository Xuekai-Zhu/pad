def solution():
    miles_per_day = 3  # Molly rode 3 miles per day
    years_riding = 16 - 13  # Molly rode for 3 years
    days_per_year = 365  # There are 365 days in a year

    # Calculate the total number of miles Molly rode
    total_miles = miles_per_day * days_per_year * years_riding
    result = total_miles
    return result

print(solution())