def solution():
    """Gavin has had 4 dreams every day for a year now. If he had twice as many dreams last year as he had this year, calculate the total number of dreams he's had in the two years."""
    dreams_per_day = 4
    days_in_year = 365
    this_year_dreams = dreams_per_day * days_in_year
    last_year_dreams = 2 * this_year_dreams
    total_dreams = this_year_dreams + last_year_dreams
    result = total_dreams
    return result

print(solution())