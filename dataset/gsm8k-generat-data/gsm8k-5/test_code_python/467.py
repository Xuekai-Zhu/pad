def solution():
    distance_to_grocery_store = 2  # Hadley walked 2 miles to the grocery store in his boots
    distance_to_pet_store = 2 - 1  # Hadley walked 1 less than 2 miles to the pet store in his boots
    distance_back_home = 4 - 1  # Hadley walked one less than 4 miles back home in his boots

    # Calculate the total distance Hadley walked in his boots
    total_distance = distance_to_grocery_store + distance_to_pet_store + distance_back_home
    result = total_distance
    return result

print(solution())