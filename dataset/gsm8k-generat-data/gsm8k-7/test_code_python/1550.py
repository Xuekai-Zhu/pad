def solution():
    daisy_seeds = 25
    sunflower_seeds = 25

    daisy_germinate_rate = 0.6
    sunflower_germinate_rate = 0.8

    flower_rate = 0.8

    # Calculate the number of daisy plants that will grow
    num_daisy_plants = daisy_seeds * daisy_germinate_rate

    # Calculate the number of sunflower plants that will grow
    num_sunflower_plants = sunflower_seeds * sunflower_germinate_rate

    # Calculate the number of daisy plants that will produce flowers
    num_flowering_daisies = num_daisy_plants * flower_rate

    # Calculate the number of sunflower plants that will produce flowers
    num_flowering_sunflowers = num_sunflower_plants * flower_rate

    # Calculate the total number of plants that will produce flowers
    total_flowering_plants = num_flowering_daisies + num_flowering_sunflowers
    result = total_flowering_plants
    return result

print(solution())