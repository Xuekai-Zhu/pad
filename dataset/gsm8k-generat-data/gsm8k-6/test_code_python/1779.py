def solution():
    # Calculate the number of dreams Gavin had this year
    dreams_this_year = 4 * 365  # Gavin has had 4 dreams every day for a year

    # Calculate the number of dreams Gavin had last year
    dreams_last_year = 2 * dreams_this_year

    # Calculate the total number of dreams Gavin has had in the two years
    total_dreams = dreams_this_year + dreams_last_year
    result = total_dreams
    return result

print(solution())