def solution():
    """Hadley wore his cowboy boots everywhere. He walked 2 miles to the grocery store in his boots. Then he walked 1 less than two miles to the pet store in his boots. Then, he walked one less than four miles back home in his boots. How far, in miles, did Hadley walk in his boots?"""
    # Calculate the distance walked to the grocery store
    grocery_distance = 2

    # Calculate the distance walked to the pet store
    pet_distance = 2 - 1

    # Calculate the distance walked back home
    home_distance = 4 - 1

    # Calculate the total distance walked
    total_distance = grocery_distance + pet_distance + home_distance

    result = total_distance
    return result

print(solution())