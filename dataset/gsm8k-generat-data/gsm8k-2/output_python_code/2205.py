def solution():
    """Shanna planted 6 tomato plants, 2 eggplant plants, and 4 pepper plants in her summer garden. Half of her tomato plants and one pepper plant died. The remaining plants each gave her 7 vegetables. How many vegetables did she have in all to harvest?"""
    tomato_plants = 6
    eggplant_plants = 2
    pepper_plants = 4

    # calculate number of plants after deaths
    tomato_plants_remaining = tomato_plants // 2
    pepper_plants_remaining = pepper_plants - 1

    # calculate total number of vegetables
    total_vegetables = (tomato_plants_remaining + eggplant_plants + pepper_plants_remaining) * 7

    result = total_vegetables
    return result

print(solution())