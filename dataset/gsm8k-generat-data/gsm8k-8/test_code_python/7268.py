def solution():
    # Define the number of cows and foxes
    cows = 20
    foxes = 15
    
    # Calculate the number of zebras
    zebras = 3 * foxes
    
    # Calculate the total number of animals
    total_animals = cows + foxes + zebras
    
    # Calculate the number of sheep needed to reach a total of 100 animals
    sheep = 100 - total_animals
    
    result = sheep
    return result

print(solution())