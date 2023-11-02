def solution():
    last_years_production = 5000
    this_years_production = last_years_production * 2
    phones_sold = this_years_production / 4
    phones_left = this_years_production - phones_sold
    result = phones_left
    
    return result

print(solution())