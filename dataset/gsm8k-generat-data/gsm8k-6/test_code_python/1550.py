def solution():
    # Calculate the number of daisy plants that will produce flowers
    daisy_plants = 25 * 0.6  # 60% of the daisy seeds germinate
    daisy_flower_plants = daisy_plants * 0.8  # 80% of resulting daisy plants produce flowers

    # Calculate the number of sunflower plants that will produce flowers
    sunflower_plants = 25 * 0.8  # 80% of the sunflower seeds germinate
    sunflower_flower_plants = sunflower_plants * 0.8  # 80% of resulting sunflower plants produce flowers

    # Calculate the total number of plants that will produce flowers
    total_flower_plants = daisy_flower_plants + sunflower_flower_plants
    result = total_flower_plants
    return result

print(solution())