def solution():
    
    initial_production = 3000
    doubling_factor = 2
    production_in_july = initial_production * (doubling_factor ** 4)
    result = production_in_july
    return result

print(solution())