def solution():
    # Calculate the number of germinated daisy seeds
    daisy_germinated = 0.6 * 25

    # Calculate the number of germinated sunflower seeds
    sunflower_germinated = 0.8 * 25

    # Calculate the total number of plants that produce flowers
    flowers_produced = 0.8 * (daisy_germinated + sunflower_germinated)

    result = flowers_produced
    return result

print(solution())