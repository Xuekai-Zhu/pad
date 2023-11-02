def solution():
    magnet_cost = 3  # cost of the red horseshoe magnet is $3
    sticker_cost = magnet_cost / 3  # magnet costs three times more than the sticker
    combined_stuffed_animals_cost = 4 * magnet_cost  # magnet costs one quarter the price of the two stuffed animals combined
    stuffed_animal_cost = (combined_stuffed_animals_cost - magnet_cost) / 2  # get the cost of a single stuffed animal
    result = stuffed_animal_cost
    return result

print(solution())