def solution():
    anthony_cats = 12 * (2/3)
    anthony_dogs = 12 * (1/3)
    leonel_cats = anthony_cats * 2
    leonel_dogs = anthony_dogs + 7
    total_cats = anthony_cats + leonel_cats
    total_dogs = anthony_dogs + leonel_dogs
    total_animals = total_cats + total_dogs
    result = total_animals
    return result

print(solution())