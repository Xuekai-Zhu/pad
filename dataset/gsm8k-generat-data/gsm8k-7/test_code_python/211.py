def solution():
    last_year_rent = 1000 * 12
    last_year_food = 200 * 12
    last_year_insurance = 100 * 12
    
    this_year_rent = last_year_rent * 1.3
    this_year_food = last_year_food * 1.5
    this_year_insurance = last_year_insurance * 3
    
    total_last_year = last_year_rent + last_year_food + last_year_insurance
    total_this_year = this_year_rent + this_year_food + this_year_insurance
    
    extra_expenses = total_this_year - total_last_year
    result = extra_expenses
    return result

print(solution())