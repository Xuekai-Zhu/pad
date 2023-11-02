def solution():
    total_weight = 1200
    num_squads = 10
    orcs_per_squad = 8

    # Calculate the total number of orcs
    total_orcs = num_squads * orcs_per_squad

    # Calculate the weight each orc needs to carry
    weight_per_orc = total_weight / total_orcs
    result = weight_per_orc
    return result

print(solution())