def solution():
    dreams_per_day = 4  # Gavin has 4 dreams every day
    days_per_year = 365  # There are 365 days in a year
    dreams_this_year = dreams_per_day * days_per_year  # Calculate the total number of dreams Gavin had this year

    # Calculate the total number of dreams Gavin had last year
    dreams_last_year = 2 * dreams_this_year

    # Calculate the total number of dreams Gavin has had in the two years
    total_dreams = dreams_this_year + dreams_last_year
    result = total_dreams
    return result

print(solution())