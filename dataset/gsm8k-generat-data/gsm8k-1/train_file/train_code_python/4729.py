def solution():
    """There are twice as many cows as dogs at a petting farm. If there are currently 184 cows at the farm, and the farm owner decides to sell 1/4 of the cows and 3/4 of the dogs, how many animals are remaining on the farm?"""
    cows = 184
    dogs = cows/2
    cows_sold = cows/4
    dogs_sold = dogs*3/4
    remaining_cows = cows - cows_sold
    remaining_dogs = dogs - dogs_sold
    total_animals = remaining_cows + remaining_dogs
    result = total_animals
    return result

print(solution())