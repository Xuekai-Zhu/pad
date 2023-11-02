def solution():
     flowers_to_plant = 20
     estimated_seeds_needed = flowers_to_plant / 2
     seeds_per_pack = 25
     packs_needed = math.ceil(estimated_seeds_needed / seeds_per_pack)
     cost_of_seeds = packs_needed * 5
     result = cost_of_seeds
 
     return result

print(solution())