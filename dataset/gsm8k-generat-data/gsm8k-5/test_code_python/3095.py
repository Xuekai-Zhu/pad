def solution():
    # Calculate the number of penguins
    penguins = 0.2 * (5 + 2 * 5)  # Penguins make up 20% of all the animals, and there are twice as many penguins as giraffes

    # Calculate the total number of animals
    total_animals = 5 + 2 * 5 + penguins  # There are 5 giraffes, twice as many penguins, and some other animals

    # Calculate the number of elephants
    elephants = 0.04 * total_animals  # Elephants make up 4% of all the animals

    result = elephants
    return result

print(solution())