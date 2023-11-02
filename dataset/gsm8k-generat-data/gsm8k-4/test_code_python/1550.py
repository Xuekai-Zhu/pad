def solution():
    """Hortense loves daisies and sunflowers. She planted 25 daisy seeds and 25 sunflower seeds in her flower bed. If 60% of the daisy seeds germinate, and 80% of the sunflower seeds germinate, and 80% of the resulting plants produce flowers, how many plants will she grow that produce flowers?"""
    # Define the number of daisy and sunflower seeds
    daisy_seeds = 25
    sunflower_seeds = 25

    # Calculate the number of germinated daisy and sunflower seeds
    germinated_daisy_seeds = daisy_seeds * 0.6
    germinated_sunflower_seeds = sunflower_seeds * 0.8

    # Calculate the total number of plants
    total_plants = germinated_daisy_seeds + germinated_sunflower_seeds

    # Calculate the number of plants that produce flowers
    flowering_plants = total_plants * 0.8

    # return the result
    result = flowering_plants
    return result

print(solution())