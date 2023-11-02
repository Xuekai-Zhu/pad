def solution():
    
    sunflowers = 6
    dandelions = 8
    sunflower_seeds = sunflowers * 9
    dandelion_seeds = dandelions * 12
    total_seeds = sunflower_seeds + dandelion_seeds
    percentage_dandelion_seeds = (dandelion_seeds / total_seeds) * 100
    result = percentage_dandelion_seeds
    
    return result

print(solution())