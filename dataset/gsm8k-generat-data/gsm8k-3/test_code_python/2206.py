def solution():
    """Shanna planted 6 tomato plants, 2 eggplant plants, and 4 pepper plants in her summer garden. Half of her tomato plants and one pepper plant died. The remaining plants each gave her 7 vegetables. How many vegetables did she have in all to harvest?"""
    # Define the number of initial plants
    initial_plants = 6 + 2 + 4

    # Calculate the number of remaining tomato plants and pepper plants
    remaining_tomato_plants = 6 / 2
    remaining_pepper_plants = 4 - 1

    # Calculate the total number of remaining plants
    remaining_plants = remaining_tomato_plants + 2 + remaining_pepper_plants

    # Calculate the total number of vegetables harvested
    total_vegetables = remaining_plants * 7

    # Display the total number of vegetables harvested
    result = total_vegetables
    return result

print(solution())