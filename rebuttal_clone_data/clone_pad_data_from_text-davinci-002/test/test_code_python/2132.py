def solution():
    age_join = 18
    years_to_chief = 8
    years_to_master_chief = years_to_chief * 1.25
    years_after_master_chief = 10
    total_years = years_to_chief + years_to_master_chief + years_after_master_chief
    age_retire = age_join + total_years
    result = age_retire
    
    return result

print(solution())