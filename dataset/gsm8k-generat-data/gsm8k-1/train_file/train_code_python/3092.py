def solution():
    """Madeline wants to plant 20 flowers in her garden. She assumes that about half of the seeds she plants will die before they bloom. However, the flower shop only sells packs of seeds with 25 seeds per pack. Each pack is $5. How much will Madeline spend on seeds to plant 20 flowers?"""
    seeds_per_pack = 25
    packs_needed = 1 + (20 / (seeds_per_pack / 2))
    cost_per_pack = 5
    total_cost = packs_needed * cost_per_pack
    result = total_cost
    return result

print(solution())