def solution():
    """In a field where there are 200 animals, there are 40 cows, 56 sheep and goats. How many goats are there?"""
    # Define the total number of animals and the number of cows and sheep
    total_animals = 200
    cows = 40
    sheep = 56

    # Calculate the number of goats
    goats = total_animals - cows - sheep

    # Return the result
    result = goats
    return result

print(solution())