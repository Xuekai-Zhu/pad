def solution():
    apples = 7
    oranges = 8
    mangoes = 15
    
    # Luisa takes out 2 apples from the bag
    apples -= 2
    
    # Luisa takes out twice as many oranges as apples
    oranges_taken = 2 * 2
    oranges -= oranges_taken
    
    # Luisa takes out 2/3 of the mangoes from the bag
    mangoes_taken = int(2/3 * mangoes)
    mangoes -= mangoes_taken
    
    # Calculate the remaining number of fruits in the bag
    remaining_fruits = apples + oranges + mangoes
    result = remaining_fruits
    return result

print(solution())