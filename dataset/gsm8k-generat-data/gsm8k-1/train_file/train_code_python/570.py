def solution():
    """Anthony and his friend Leonel read about the importance of keeping pets at home and decided to start adopting cats and dogs from the local rescue center. Anthony has 12 cats and dogs, 2/3 of which are cats. Leonel has half times as many cats as Anthony and seven more dogs than Anthony. How many animals in total do the two have?"""
    anthony_total = 12
    anthony_cats = anthony_total * (2/3)
    anthony_dogs = anthony_total - anthony_cats
    
    leonel_cats = anthony_cats / 2
    leonel_dogs = anthony_dogs + 7
    
    total_animals = anthony_total + leonel_cats + leonel_dogs
    
    result = total_animals
    
    return result

print(solution())