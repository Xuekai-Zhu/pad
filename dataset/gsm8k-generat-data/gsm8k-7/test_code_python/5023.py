def solution():
    total_swords_weight = 1200
    num_orc_squads = 10
    num_orcs_per_squad = 8
    
    # Calculate the total number of orcs
    total_orcs = num_orc_squads * num_orcs_per_squad
    
    # Calculate the weight of swords each orc has to carry
    weight_per_orc = total_swords_weight/total_orcs
    result = weight_per_orc
    return result

print(solution())