def solution():
    """Jan has three times the number of pets as Marcia. Marcia has two more pets than Cindy. If Cindy has four pets, how many total pets do the three have?"""
    cindy_pets = 4
    marcia_pets = cindy_pets + 2
    jan_pets = marcia_pets * 3
    total_pets = cindy_pets + marcia_pets + jan_pets
    result = total_pets
    return result

print(solution())