def solution():
    
    year_1_production = 10 * 365
    year_2_production = year_1_production - (0.1 * year_1_production)
    result = year_2_production
    return result

print(solution())