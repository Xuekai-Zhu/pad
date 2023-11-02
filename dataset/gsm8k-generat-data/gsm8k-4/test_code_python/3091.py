def solution():
    """Marcy had 22 sodas in her fridge for a party. Her friend Tina came over and gave her 12 plus two times the number of sodas Marcy had before. How many sodas will Marcy have for the party?"""
    # Define the initial number of sodas
    initial_sodas = 22
    
    # Calculate the number of sodas Tina gave
    tina_sodas = 12 + 2*initial_sodas
    
    # Calculate the total number of sodas for the party
    total_sodas = initial_sodas + tina_sodas
    
    # return the result
    result = total_sodas
    return result

print(solution())