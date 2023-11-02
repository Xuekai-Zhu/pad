def solution():
    """In a field where there are 200 animals, there are 40 cows, 56 sheep and goats. How many goats are there?"""
    # Define the total number of animals and the number of cows and sheep
    total_animals = 200
    num_cows = 40
    num_sheep = 56

    # Calculate the number of goats
    num_goats = total_animals - num_cows - num_sheep

    # Display the number of goats
    result = num_goats
    return result

print(solution())