def solution():
    """Hadley wore his cowboy boots everywhere. He walked 2 miles to the grocery store in his boots. Then he walked 1 less than two miles to the pet store in his boots. Then, he walked one less than four miles back home in his boots. How far, in miles, did Hadley walk in his boots?"""
    distance_to_grocery_store = 2
    distance_to_pet_store = 2 - 1
    distance_back_home = 4 - 1
    total_distance = distance_to_grocery_store + distance_to_pet_store + distance_back_home
    result = total_distance
    return result

print(solution())