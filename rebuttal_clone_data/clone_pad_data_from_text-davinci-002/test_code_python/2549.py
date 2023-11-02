def solution():
    iron = 400
    farms = 2
    horses_per_farm = 2
    stables = 2
    horses_per_stable = 5
    horseshoes = iron / 2
    total_horseshoes = horseshoes - (farms * horses_per_farm) - (stables * horses_per_stable)
    result = total_horseshoes
    return result

print(solution())