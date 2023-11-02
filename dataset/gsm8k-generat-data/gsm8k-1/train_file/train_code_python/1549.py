def solution():
    """Hortense loves daisies and sunflowers. She planted 25 daisy seeds and 25 sunflower seeds in her flower bed. If 60% of the daisy seeds germinate, and 80% of the sunflower seeds germinate, and 80% of the resulting plants produce flowers, how many plants will she grow that produce flowers?"""
    daisy_seeds = 25
    sunflower_seeds = 25
    daisy_germination_rate = 0.6
    sunflower_germination_rate = 0.8
    flower_production_rate = 0.8
    daisy_plants = daisy_seeds * daisy_germination_rate * flower_production_rate
    sunflower_plants = sunflower_seeds * sunflower_germination_rate * flower_production_rate
    total_plants = daisy_plants + sunflower_plants
    result = total_plants
    return result

print(solution())