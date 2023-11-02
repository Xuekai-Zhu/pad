def solution():
    # Define the total number of animals the farmer has
    total_animals = 56
    
    # Calculate the number of cows
    cows = (total_animals - 4) / 3
    
    # Calculate the number of pigs (twice as many as cows)
    pigs = 2 * cows
    
    # Calculate the number of goats (4 fewer than cows)
    goats = cows - 4
    
    result = goats
    return result

print(solution())