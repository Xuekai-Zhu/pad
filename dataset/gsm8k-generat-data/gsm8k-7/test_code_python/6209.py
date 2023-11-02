def solution():
    num_basil_bushes = 3
    extra_basil_plant = 1
    num_parsley_plants = 1
    num_mint_plants = 2
    rabbit_damage = num_mint_plants

    # Calculate the total number of basil plants at the end of spring
    total_basil_plants = num_basil_bushes + extra_basil_plant

    # Calculate the total number of herb plants at the end of spring
    total_herb_plants = total_basil_plants + num_parsley_plants + num_mint_plants - rabbit_damage
    result = total_herb_plants
    return result

print(solution())