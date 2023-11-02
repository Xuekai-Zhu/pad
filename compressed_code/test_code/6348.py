def solution():
    
    legs_per_tarantula = 8
    tarantulas_per_sac = 1000
    num_sacs = 5 - 1
    num_tarantulas = num_sacs * tarantulas_per_sac
    num_legs = num_tarantulas * legs_per_tarantula
    result = num_legs
    return result

print(solution())