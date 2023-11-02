def solution():
    total_animals = 0
    anthony_cats = 12 * 2 / 3  # Anthony has 2/3 of 12 animals as cats
    anthony_dogs = 12 - anthony_cats  # The remaining animals are dogs
    
    leonel_cats = anthony_cats / 2  # Leonel has half as many cats as Anthony
    leonel_dogs = anthony_dogs + 7  # Leonel has seven more dogs than Anthony
    
    total_animals = anthony_cats + anthony_dogs + leonel_cats + leonel_dogs 
    
    result = total_animals
    return result

print(solution())