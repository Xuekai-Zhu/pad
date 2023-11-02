def solution():
    total_animals = 24 + 7  # Total animals Zara bought
    groups = 3  # Number of equally-sized groups
    animals_per_group = 48  # Number of animals per group
    
    # Calculate the total number of animals transported
    total_transport = groups * animals_per_group
    
    # Calculate the number of goats Zara owns
    goats = total_transport - total_animals
    result = goats
    return result

print(solution())