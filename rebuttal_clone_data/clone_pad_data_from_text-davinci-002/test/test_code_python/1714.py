def solution():
     sunflowers = 6
     dandelions = 8
     seeds_per_sunflower = 9
     seeds_per_dandelion = 12
     total_seeds = (sunflowers * seeds_per_sunflower) + (dandelions * seeds_per_dandelion)
     dandelion_seeds = dandelions * seeds_per_dandelion
     percent = (dandelion_seeds / total_seeds) * 100
     result = percent
     
     return result

print(solution())