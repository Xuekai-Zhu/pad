def solution():
    
    anthony_cats = 2/3 * 12
    anthony_dogs = 12 - anthony_cats
    leonel_cats = 1/2 * anthony_cats
    leonel_dogs = anthony_dogs + 7
    total_animals = anthony_cats + anthony_dogs + leonel_cats + leonel_dogs
    result = total_animals
    return result

print(solution())