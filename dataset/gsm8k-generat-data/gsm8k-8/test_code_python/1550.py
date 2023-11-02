def solution():
    # Calculate number of germinated daisy seeds and sunflower seeds
    daisy_germinated = 0.6 * 25
    sunflower_germinated = 0.8 * 25

    # Calculate number of plants grown from germinated seeds
    daisy_plants = 0.8 * daisy_germinated
    sunflower_plants = 0.8 * sunflower_germinated

    # Calculate total number of plants that produce flowers
    total_plants = daisy_plants + sunflower_plants

    result = total_plants
    return result

print(solution())