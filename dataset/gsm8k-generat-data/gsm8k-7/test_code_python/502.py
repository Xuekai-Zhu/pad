def solution():
    magnet_cost = 3
    sticker_cost = magnet_cost / 3
    stuffed_animals_cost = 4 * magnet_cost
    total_cost = magnet_cost + 2 * stuffed_animals_cost + sticker_cost
    single_stuffed_animal_cost = (total_cost - magnet_cost - sticker_cost) / 2
    result = single_stuffed_animal_cost
    return result

print(solution())