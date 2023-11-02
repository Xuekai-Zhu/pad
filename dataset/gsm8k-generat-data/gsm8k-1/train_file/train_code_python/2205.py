def solution():
    """Shanna planted 6 tomato plants, 2 eggplant plants, and 4 pepper plants in her summer garden. Half of her tomato plants and one pepper plant died. The remaining plants each gave her 7 vegetables. How many vegetables did she have in all to harvest?"""
    tomato_plants = 6
    eggplant_plants = 2
    pepper_plants = 4

    # Calculate how many plants were lost
    lost_tomato_plants = tomato_plants / 2
    lost_pepper_plants = 1

    # Calculate how many plants are remaining
    remaining_tomato_plants = tomato_plants - lost_tomato_plants
    remaining_pepper_plants = pepper_plants - lost_pepper_plants

    # Calculate the total number of vegetables harvested
    total_vegetables = (remaining_tomato_plants + eggplant_plants + remaining_pepper_plants) * 7

    result = total_vegetables
    return result

print(solution())