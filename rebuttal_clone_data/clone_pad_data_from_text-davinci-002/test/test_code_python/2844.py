def solution():
    total_weight = 1200
    num_squads = 10
    orcs_per_squad = 8
    weight_per_orc = total_weight / (num_squads * orcs_per_squad)
    result = weight_per_orc
    return result

print(solution())