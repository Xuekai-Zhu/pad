def solution():
    """Hortense loves daisies and sunflowers.  She planted 25 daisy seeds and 25 sunflower seeds in her flower bed.  If 60% of the daisy seeds germinate, and 80% of the sunflower seeds germinate, and 80% of the resulting plants produce flowers, how many plants will she grow that produce flowers?"""
    # Define the percentage of germination and flower production for each type of seed
    DAISY_GERMINATION_PERCENT = 0.6
    SUNFLOWER_GERMINATION_PERCENT = 0.8
    FLOWER_PRODUCTION_PERCENT = 0.8

    # Define the number of seeds planted
    daisy_seeds = 25
    sunflower_seeds = 25

    # Calculate the number of plants that germinate and produce flowers for each type of seed
    daisy_plants = round(daisy_seeds * DAISY_GERMINATION_PERCENT * FLOWER_PRODUCTION_PERCENT)
    sunflower_plants = round(sunflower_seeds * SUNFLOWER_GERMINATION_PERCENT * FLOWER_PRODUCTION_PERCENT)

    # Calculate the total number of plants that produce flowers
    total_plants = daisy_plants + sunflower_plants

    # Display the total number of plants that produce flowers
    result = total_plants
    return result

print(solution())