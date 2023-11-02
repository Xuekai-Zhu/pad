def solution():
    
    last_year_rent = 1000 * 12
    last_year_food = 200 * 12
    last_year_insurance = 100 * 12
    
    new_rent = 1000 * 1.3 * 12
    new_food = 200 * 1.5 * 12
    new_insurance = 100 * 3 * 12
    
    total_last_year = last_year_rent + last_year_food + last_year_insurance
    total_new = new_rent + new_food + new_insurance
    
    difference = total_new - total_last_year
    
    result = difference
    return result

print(solution())