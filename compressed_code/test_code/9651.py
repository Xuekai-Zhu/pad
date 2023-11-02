def solution():
    
    apples = 7
    oranges = 8
    mangoes = 15
    
    
    apples -= 2
    
    
    oranges_taken = 2 * 2 
    oranges -= oranges_taken
    
    
    mangoes_taken = int(2/3 * mangoes)
    mangoes -= mangoes_taken
    
    
    remaining_fruits = apples + oranges + mangoes
    
    result = remaining_fruits
    return result

print(solution())