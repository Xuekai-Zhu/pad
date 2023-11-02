def solution():
    
    daisy_seeds = 25
    sunflower_seeds = 25
    daisy_germination_rate = 0.6
    sunflower_germination_rate = 0.8
    flower_percentage = 0.8
    daisy_plants = daisy_seeds * daisy_germination_rate
    sunflower_plants = sunflower_seeds * sunflower_germination_rate
    total_plants = daisy_plants + sunflower_plants
    flower_plants = total_plants * flower_percentage
    result = flower_plants
    return result

print(solution())