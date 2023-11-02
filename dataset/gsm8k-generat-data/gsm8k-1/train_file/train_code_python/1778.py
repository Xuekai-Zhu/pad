def solution():
    """Gavin has had 4 dreams every day for a year now. If he had twice as many dreams last year as he had this year, calculate the total number of dreams he's had in the two years."""
    dreams_per_day = 4
    days_per_year = 365
    dreams_this_year = dreams_per_day * days_per_year
    dreams_last_year = dreams_this_year * 2
    total_dreams = dreams_this_year + dreams_last_year
    result = total_dreams
    return result

print(solution())