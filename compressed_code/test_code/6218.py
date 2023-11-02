def solution():
    
    anthony_total = 12
    anthony_cats = anthony_total * (2/3)
    anthony_dogs = anthony_total - anthony_cats
    
    leonel_cats = anthony_cats / 2
    leonel_dogs = anthony_dogs + 7
    
    total_animals = anthony_total + leonel_cats + leonel_dogs
    
    result = total_animals
    
    return result

print(solution())