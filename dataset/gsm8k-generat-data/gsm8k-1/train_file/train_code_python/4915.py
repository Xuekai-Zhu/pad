def solution():
    """A bag has seven apples, eight oranges, and 15 mangoes. Luisa takes out two apples from the bag, 
    and takes out twice as many oranges as apples as she took from the bag. She then takes out 
    2/3 the number of mangoes from the bag. What is the remaining number of fruits in the bag?"""
    apples = 7
    oranges = 8
    mangoes = 15
    
    # Luisa takes out two apples
    apples -= 2
    
    # Luisa takes out twice as many oranges as she took apples
    oranges_taken = 2 * 2 # Luisa took out 4 oranges
    oranges -= oranges_taken
    
    # Luisa takes out 2/3 of the mangoes
    mangoes_taken = int(2/3 * mangoes)
    mangoes -= mangoes_taken
    
    # Total remaining fruits in the bag
    remaining_fruits = apples + oranges + mangoes
    
    result = remaining_fruits
    return result

print(solution())