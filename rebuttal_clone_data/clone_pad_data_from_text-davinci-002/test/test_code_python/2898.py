def solution():
    initial_production = 3000
    production_doubled = 2
    month_of_production = 4
    total_production = initial_production * (production_doubled ** month_of_production)
    result = total_production
    
    return result

print(solution())