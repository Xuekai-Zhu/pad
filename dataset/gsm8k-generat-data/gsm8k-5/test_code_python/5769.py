def solution():
    total_animals = 24 + 7  # Zara has 24 cows and 7 sheep
    total_groups = 3  # Zara will transport all animals in 3 equally-sized groups
    animals_per_group = 48  # Each group will have 48 animals

    # Calculate the total number of animals that need to be transported
    total_transport_animals = total_groups * animals_per_group

    # Calculate the number of goats that Zara owns
    goats = total_transport_animals - total_animals
    result = goats
    return result

print(solution())