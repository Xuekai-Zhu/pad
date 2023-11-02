def solution():
    """Frankie's parents let him have many pets. He has six more snakes than he has cats. He has one less parrot than cats. Six of his pets have four legs. He has 2 dogs. How many pets does he have in total?"""
    # Let's denote the number of cats as x
    x = (6 + 1) / 2

    # Calculate the number of snakes and parrots
    snakes = x + 6
    parrots = x - 1

    # Calculate the number of pets with four legs
    four_legs = 2 + x + snakes + parrots

    # Calculate the total number of pets
    total_pets = four_legs + (snakes - x) + (parrots - x)

    # Display the total number of pets
    result = total_pets
    return result

print(solution())