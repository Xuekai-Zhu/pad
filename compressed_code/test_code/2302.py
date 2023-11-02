def solution():
    
    current_kate_age = 29
    tully_age_in_3_years = 2 * (current_kate_age + 3)
    current_tully_age = tully_age_in_3_years - 3
    tully_age_a_year_ago = current_tully_age - 1
    result = tully_age_a_year_ago
    return result

print(solution())