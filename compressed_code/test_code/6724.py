def solution():
    
    total_packs = 20
    doug_age = 40
    total_age = 90
    betty_age = total_age - doug_age
    cost_per_pack = betty_age * 2
    total_cost = cost_per_pack * total_packs
    result = total_cost
    return result

print(solution())