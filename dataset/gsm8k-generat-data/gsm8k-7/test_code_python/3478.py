def solution():
    num_people = 8
    num_smores_per_person = 3
    num_smores_total = num_people * num_smores_per_person
    smores_per_supply_pack = 4
    cost_per_supply_pack = 3
    num_supply_packs = (num_smores_total + smores_per_supply_pack - 1) // smores_per_supply_pack  # rounding up division
    total_cost = num_supply_packs * cost_per_supply_pack
    result = total_cost
    return result

print(solution())