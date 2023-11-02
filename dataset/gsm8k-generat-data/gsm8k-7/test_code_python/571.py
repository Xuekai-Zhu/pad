def solution():
    anthony_cats = 2/3 * 12
    anthony_dogs = 12 - anthony_cats

    leonel_cats = 1/2 * anthony_cats
    leonel_dogs = anthony_dogs + 7

    total_cats = anthony_cats + leonel_cats
    total_dogs = anthony_dogs + leonel_dogs

    total_animals = total_cats + total_dogs
    result = total_animals
    return result

print(solution())