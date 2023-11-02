def solution():
    magnet_cost = 3  # The magnet costs $3
    sticker_cost = magnet_cost / 3  # The magnet costs three times more than the sticker
    combined_animal_cost = magnet_cost / 0.25  # The magnet costs one quarter the price of the two stuffed animals combined

    # Calculate the total cost of all items
    total_cost = magnet_cost + sticker_cost + combined_animal_cost

    # Calculate the cost of a single stuffed animal
    single_animal_cost = (total_cost - magnet_cost - sticker_cost) / 2
    result = single_animal_cost
    return result

print(solution())