def solution():
    """Hadley wore his cowboy boots everywhere. He walked 2 miles to the grocery store in his boots. Then he walked 1 less than two miles to the pet store in his boots. Then, he walked one less than four miles back home in his boots. How far, in miles, did Hadley walk in his boots?"""
    grocery_store_distance = 2
    pet_store_distance = 2 - 1
    home_distance = 4 - 1
    total_distance = grocery_store_distance + pet_store_distance + home_distance
    result = total_distance
    return result

print(solution())