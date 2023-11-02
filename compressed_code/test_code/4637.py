def solution():
    
    year_one_production = 40
    year_two_production = 8 + 2 * year_one_production
    year_three_production = 0.75 * year_two_production
    total_production = year_one_production + year_two_production + year_three_production
    result = total_production
    return result

print(solution())