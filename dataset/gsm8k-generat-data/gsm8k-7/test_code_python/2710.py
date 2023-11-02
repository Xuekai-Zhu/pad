def solution():
    current_cows = 2
    current_pigs = 3
    current_goats = 6
    
    new_cows = 3
    new_pigs = 5
    new_goats = 2
    
    # Calculate the total number of cows after adding new ones
    total_cows = current_cows + new_cows
    
    # Calculate the total number of pigs after adding new ones
    total_pigs = current_pigs + new_pigs
    
    # Calculate the total number of goats after adding new ones
    total_goats = current_goats + new_goats
    
    # Calculate the total number of animals on the farm
    total_animals = total_cows + total_pigs + total_goats
    result = total_animals
    return result

print(solution())