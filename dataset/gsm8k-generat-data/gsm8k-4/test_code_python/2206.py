def solution():
    """Shanna planted 6 tomato plants, 2 eggplant plants, and 4 pepper plants in her summer garden. Half of her tomato plants and one pepper plant died. The remaining plants each gave her 7 vegetables. How many vegetables did she have in all to harvest?"""
    # Define the initial number of plants
    tomato_plants = 6
    eggplant_plants = 2
    pepper_plants = 4

    # Calculate the number of plants that died
    dead_tomato_plants = tomato_plants / 2
    dead_pepper_plants = 1

    # Calculate the number of remaining plants
    remaining_tomato_plants = tomato_plants - dead_tomato_plants
    remaining_pepper_plants = pepper_plants - dead_pepper_plants

    # Calculate the total number of vegetables harvested
    total_vegetables = remaining_tomato_plants * 7 + eggplant_plants * 7 + remaining_pepper_plants * 7

    # return the result
    result = total_vegetables
    return result

print(solution())