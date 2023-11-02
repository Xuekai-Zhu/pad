def solution():
    total_daisy_seeds = 25
    total_sunflower_seeds = 25
    germination_rate_daisy = .6
    germination_rate_sunflower = .8
    flower_production_rate = .8
    total_daisy_plants = total_daisy_seeds * germination_rate_daisy
    total_sunflower_plants = total_sunflower_seeds * germination_rate_sunflower
    total_flowering_daisy_plants = total_daisy_plants * flower_production_rate
    total_flowering_sunflower_plants = total_sunflower_plants * flower_production_rate
    total_flowering_plants = total_flowering_daisy_plants + total_flowering_sunflower_plants
    result = total_flowering_plants
    
    return result

print(solution())