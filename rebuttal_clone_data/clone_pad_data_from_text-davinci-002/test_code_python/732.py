def solution():
    legs_per_tarantula = 8
    tarantulas_per_egg_sac = 1000
    egg_sacs = 4
    total_tarantulas = tarantulas_per_egg_sac * egg_sacs
    total_legs = total_tarantulas * legs_per_tarantula
    result = total_legs
    return result

print(solution())