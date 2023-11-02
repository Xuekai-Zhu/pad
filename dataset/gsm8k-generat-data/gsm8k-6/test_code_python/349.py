def solution():
    total_animals = 56
    # Let's assume the number of goats is x
    goats = x
    
    # The number of cows will be 4 more than the goats
    cows = goats + 4
    
    # The number of pigs is twice that of cows
    pigs = 2 * cows
    
    # Total number of animals
    total = goats + cows + pigs
    
    # Now we can solve for x
    # goats + goats + 4 + 2* (goats + 4) = 56
    # 4goats + 12 = 56
    # 4goats = 44
    goats = 11
    
    result = goats
    return result

print(solution())