def solution():
    original_flock_size = 100
    ducks_killed_per_year = 20
    ducks_born_per_year = 30
    number_of_years = 5
    net_change_per_year = ducks_born_per_year - ducks_killed_per_year
    size_of_flock_after_5_years = original_flock_size + (net_change_per_year * number_of_years)
    combined_flock_size = size_of_flock_after_5_years + 150
    result = combined_flock_size
    
    return result

print(solution())