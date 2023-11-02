def solution():
    
    dreams_per_day = 4
    days_per_year = 365
    dreams_this_year = dreams_per_day * days_per_year
    dreams_last_year = dreams_this_year * 2
    total_dreams = dreams_this_year + dreams_last_year
    result = total_dreams
    return result

print(solution())