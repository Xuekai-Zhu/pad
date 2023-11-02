def solution():
    hair_cut_length = 6
    current_hair_length = 36
    monthly_growth_rate = .5
    total_growth = current_hair_length - hair_cut_length
    number_of_months = total_growth / monthly_growth_rate
    number_of_years = number_of_months / 12
    result = number_of_years
    
    return result

print(solution())