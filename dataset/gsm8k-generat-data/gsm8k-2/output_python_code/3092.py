def solution():
    """Madeline wants to plant 20 flowers in her garden. She assumes that about half of the seeds she plants will die before they bloom. However, the flower shop only sells packs of seeds with 25 seeds per pack. Each pack is $5. How much will Madeline spend on seeds to plant 20 flowers?"""
    seeds_per_flower = 2
    total_seeds_needed = seeds_per_flower * 20
    seeds_per_pack = 25
    packs_needed = (total_seeds_needed // seeds_per_pack) + 1
    pack_price = 5
    total_price = packs_needed * pack_price
    result = total_price
    return result

print(solution())