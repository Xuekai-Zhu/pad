def solution():
    
    drops_per_liter = 5000
    liters_to_die = 3
    drops_to_die = drops_per_liter * liters_to_die
    drops_per_bite = 20
    mosquitos_to_die = drops_to_die / drops_per_bite
    result = mosquitos_to_die
    return result

print(solution())