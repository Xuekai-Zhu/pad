def solution():
    # Define the variables
    magnet_cost = 3
    sticker_cost = magnet_cost / 3
    combined_animals_cost = magnet_cost / 0.25 - magnet_cost - sticker_cost
    single_animal_cost = combined_animals_cost / 2

    result = single_animal_cost
    return result

print(solution())