def solution():
    """Anthony has 12 cats and dogs, 2/3 of which are cats. Leonel has half times as many cats as Anthony and seven more dogs than Anthony. How many animals in total do the two have?"""
    anthony_cats = 2/3 * 12
    anthony_dogs = 12 - anthony_cats
    leonel_cats = 1/2 * anthony_cats
    leonel_dogs = anthony_dogs + 7
    total_animals = anthony_cats + anthony_dogs + leonel_cats + leonel_dogs
    result = total_animals
    return result

print(solution())