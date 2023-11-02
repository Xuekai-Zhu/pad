def solution():
    """Marcy had 22 sodas in her fridge for a party. Her friend Tina came over and gave her 12 plus two times the number of sodas Marcy had before. How many sodas will Marcy have for the party?"""
    initial_sodas = 22
    tina_sodas = 12 + (2 * initial_sodas)
    total_sodas = initial_sodas + tina_sodas
    result = total_sodas
    return result

print(solution())