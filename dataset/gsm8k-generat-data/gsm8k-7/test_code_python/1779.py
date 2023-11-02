def solution():
    dreams_per_day_this_year = 4
    days_this_year = 365
    dreams_this_year = dreams_per_day_this_year * days_this_year

    dreams_last_year = dreams_this_year * 2

    total_dreams = dreams_this_year + dreams_last_year
    result = total_dreams
    return result

print(solution())