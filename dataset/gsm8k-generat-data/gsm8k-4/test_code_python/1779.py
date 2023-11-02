def solution():
    """Gavin has had 4 dreams every day for a year now. If he had twice as many dreams last year as he had this year, calculate the total number of dreams he's had in the two years."""
    # Calculate the number of dreams Gavin has had this year
    dreams_this_year = 4 * 365

    # Calculate the number of dreams Gavin had last year
    dreams_last_year = dreams_this_year / 2

    # Calculate the total number of dreams Gavin has had in the two years
    total_dreams = dreams_this_year + dreams_last_year

    # Return the result
    result = total_dreams
    return result

print(solution())