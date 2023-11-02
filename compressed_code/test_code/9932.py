def solution():
    
    last_year_production = 5000
    this_year_production = last_year_production * 2
    sold_production = this_year_production / 4
    remaining_production = this_year_production - sold_production
    result = remaining_production
    return result

print(solution())