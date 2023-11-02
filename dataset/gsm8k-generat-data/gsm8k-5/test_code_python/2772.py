def solution():
    eggplants_per_pack = 14  # Shyne can grow 14 eggplants in every seed packet
    sunflowers_per_pack = 10  # Shyne can grow 10 sunflowers in every seed packet
    eggplant_packs = 4  # Shyne bought 4 seed packets of eggplants
    sunflower_packs = 6  # Shyne bought 6 seed packets of sunflowers

    # Calculate the total number of eggplants and sunflowers Shyne can grow
    total_eggplants = eggplants_per_pack * eggplant_packs
    total_sunflowers = sunflowers_per_pack * sunflower_packs

    # Calculate the total number of plants Shyne can grow
    total_plants = total_eggplants + total_sunflowers
    result = total_plants
    return result

print(solution())