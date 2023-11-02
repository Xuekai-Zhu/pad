def solution():
    doug_age = 40
    total_age = 90
    betty_age = total_age - doug_age

    cost_per_pack = betty_age * 2
    num_packs = 20

    total_cost = cost_per_pack * num_packs
    result = total_cost
    return result

print(solution())