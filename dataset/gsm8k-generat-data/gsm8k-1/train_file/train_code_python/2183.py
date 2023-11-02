def solution():
    """Frankie's parents let him have many pets. He has six more snakes than he has cats. He has one less parrot than cats. Six of his pets have four legs. He has 2 dogs. How many pets does he have in total?"""
    cats = 5
    snakes = cats + 6
    parrots = cats - 1
    four_legged_pets = 6
    dogs = 2
    total_pets = cats + snakes + parrots + four_legged_pets + dogs
    result = total_pets
    return result

print(solution())