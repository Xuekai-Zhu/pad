def solution():
    
    legs_per_tarantula = 8
    tarantulas_per_egg_sac = 1000
    num_egg_sacs = 5 - 1
    total_tarantulas = tarantulas_per_egg_sac * num_egg_sacs
    total_legs = total_tarantulas * legs_per_tarantula
    result = total_legs
    return result

print(solution())